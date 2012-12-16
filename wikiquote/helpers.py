#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urlparse


def update_url(parse_result, **kwargs):
    """Change some part of parsed url by build new copy."""
    parse_result_dict = parse_result._asdict()
    parse_result_dict.update(**kwargs)
    return urlparse.ParseResult(**parse_result_dict)
