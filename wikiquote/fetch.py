#!/usr/bin/env python
#-*- coding:utf-8 -*-

import itertools

import requests
import lxml.html

from .consts import LANG_URL, LANG_XPATH, LANG_LABEL_XPATH
from .models import Language, QuoteId, Quote


def fetch_html(url, **kwargs):
    """Gets a url and return the response as XML element tree."""
    response = requests.get(url, **kwargs)
    etree = lxml.html.fromstring(response.text)
    return etree


def fetch_languages():
    """Gets supported languages list of wikiquote site."""
    etree = fetch_html(LANG_URL)
    anchors = etree.xpath(LANG_XPATH)
    labels = etree.xpath(LANG_LABEL_XPATH)
    for anchor, label in itertools.izip(anchors, labels):
        #: create the language model
        url = anchor.get("href")
        language = Language(name=anchor.text, label=label.text, url=url)
        yield language


def fetch_current_quote(language):
    """Gets current daily quote."""
    quote_id = QuoteId.create(language)
    quote = Quote(quote_id)

    etree = fetch_html(language.url)
    quote.quote_word = "".join(etree.xpath(quote.daily_xpath)).strip()
    return quote
