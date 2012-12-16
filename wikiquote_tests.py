#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from wikiquote.fetch import fetch_languages
from wikiquote.models import Language


class FetchTest(unittest.TestCase):
    """The test case of fetch language."""

    EXAMPLE_LANGUAGES = [
            Language(u"en", u"English", u"http://en.wikiquote.org/wiki/"),
            Language(u"zh", u"中文", u"http://zh.wikiquote.org/wiki/")]

    def test_fetch_language(self):
        languages = set(fetch_languages())
        for example in self.EXAMPLE_LANGUAGES:
            self.assertIn(example, languages)
