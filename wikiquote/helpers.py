#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urlparse


def update_url(parse_result, **kwargs):
    """Change some part of parsed url by build new copy."""
    parse_result_dict = parse_result._asdict()
    parse_result_dict.update(**kwargs)
    return urlparse.ParseResult(**parse_result_dict)


def _make_lru_cache_decorator():
    """Gets a LRU cache decorator in two selection."""
    try:
        from repoze.lru import lru_cache
    except ImportError:
        from functools import lru_cache
    return lru_cache


lru_cache = _make_lru_cache_decorator()
