#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urlparse
import collections
import datetime

from .consts import DAILY_EN_XPATH, DAILY_CN_XPATH
from .helpers import update_url


cls_super = lambda cls: cls.__bases__[0]
cls_super.__doc__ = """Get the first base of current class."""


class Language(collections.namedtuple("Language", ["name", "label", "url"])):
    """The language of wikiquote page."""

    def __new__(cls, name, label, url):
        url = cls.prepare_url(url)
        return cls_super(cls).__new__(cls, name, label, url)

    @staticmethod
    def prepare_url(url):
        if not url:
            return None
        #: apply default scheme to url
        parsed = urlparse.urlparse(url)
        modified = update_url(parsed, scheme=parsed.scheme or "https")
        return modified.geturl()


class QuoteId(collections.namedtuple("QuoteId", ["date", "language"])):
    """The identity of quote item."""

    @classmethod
    def create(cls, language):
        return cls(datetime.datetime.utcnow().date(), language)


class Quote(object):
    """The quote item of wikiquote."""

    DAILY_XPATH = {"en": DAILY_EN_XPATH, "zh": DAILY_CN_XPATH}

    def __init__(self, quote_id, quote_word=None):
        self.quote_id = quote_id
        self.quote_word = quote_word

    @property
    def daily_xpath(self):
        return self.DAILY_CN_XPATH[self.quote_id.language.name]
