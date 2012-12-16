#!/usr/bin/env python
#-*- coding:utf-8 -*-

import collections


class Language(collections.namedtuple("Language", ["name", "label", "url"])):
    """The language of wikiquote page."""
