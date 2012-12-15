#!?usr/bin/env python2

from setuptools import setup, find_packages


setup(name="wikiquote",
      description="A utility to fetch daily wikiquote.",
      version="0.1",
      requires=["requests", "lxml"],
      packages=find_packages())
