#!?usr/bin/env python2

import sys

from setuptools import setup


requires = ["requests", "lxml"]

if sys.version_info < (3,):
    # instead of functools.lrc_cache
    requires.extend(["repoze.lru"])


setup(name="wikiquote",
      description="A utility to fetch daily wikiquote.",
      version="0.1",
      author="TonySeek",
      author_email="tonyseek@gmail.com",
      packages=["wikiquote"],
      requires=requires,
      test_suite="wikiquote_tests")
