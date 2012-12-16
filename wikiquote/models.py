#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urlparse
import collections

from .helpers import update_url


class Language(collections.namedtuple("Language", ["name", "label", "url"])):
    """The language of wikiquote page."""

    def __new__(cls, name, label, url):
        url = cls.prepare_url(url)
        return cls.__bases__[0].__new__(cls, name, label, url)

    @staticmethod
    def prepare_url(url):
        if not url:
            return None
        #: apply default scheme to url
        parsed = urlparse.urlparse(url)
        modified = update_url(parsed, scheme=parsed.scheme or "https")
        return modified.geturl()
