#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urlparse
import itertools

import requests
import lxml.html

from .consts import LANG_URL, LANG_XPATH, LANG_LABEL_XPATH
from .models import Language
from .helpers import update_url


def fetch_html(url, **kwargs):
    """Gets a url and return the response as XML element tree."""
    response = requests.get(url, **kwargs)
    etree = lxml.html.fromstring(response.text)
    return etree


def fetch_languages():
    etree = fetch_html(LANG_URL)
    anchors = etree.xpath(LANG_XPATH)
    labels = etree.xpath(LANG_LABEL_XPATH)
    for anchor, label in itertools.izip(anchors, labels):
        #: apply
        href = urlparse.urlparse(anchor.get("href"))
        url = update_url(href, scheme=href.scheme or "http").geturl()
        language = Language(name=anchor.text, label=label.text, url=url)
        yield language
