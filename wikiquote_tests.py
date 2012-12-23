#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
import urlparse

import requests.models
import requests.exceptions

from wikiquote.fetch import fetch_languages, fetch_current_quote
from wikiquote.models import Language


class FetchTest(unittest.TestCase):
    """The test case of fetch language."""

    EXAMPLE_LANGUAGES = [
            Language(u"en", u"English", u"https://en.wikiquote.org/wiki/"),
            Language(u"zh", u"中文", u"https://zh.wikiquote.org/wiki/")]

    def test_fetch_language(self):
        languages = set(fetch_languages())
        #: check example
        for example in self.EXAMPLE_LANGUAGES:
            self.assertIn(example, languages)
        #: check attribute
        for language in languages:
            #: name should only contains letters or "-"
            self.assertRegexpMatches(language.name, r"[a-zA-Z-]{1,10}")
            #: label should not contains any special character
            self.assertRegexpMatches(language.label, r"[^!@#\$%\^&*()+-]+")
            #: the url should be valid
            self.assertIsNotNone(language.url)
            url = urlparse.urlparse(language.url)
            self.assertIn(url.scheme, {"http", "https"})
            self.assertRegexpMatches(url.netloc, r"[a-zA-Z-]+\.wikiquote.org")

    def test_fetch_daily(self):
        for language in self.EXAMPLE_LANGUAGES:
            quote = fetch_current_quote(language)
            self.assertRegexpMatches(quote.quote_word, r".+")
