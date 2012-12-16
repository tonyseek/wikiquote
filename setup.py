#!?usr/bin/env python2

from setuptools import setup


setup(name="wikiquote",
      description="A utility to fetch daily wikiquote.",
      version="0.1",
      author="TonySeek",
      author_email="tonyseek@gmail.com",
      packages=["wikiquote"],
      requires=["requests", "lxml"],
      test_suite="wikiquote_tests")
