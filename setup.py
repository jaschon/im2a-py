#!/usr/bin/env python3

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "im2a",
    version = "0.35",
    author = "Jason Rebuck",
    description = ("Image to Ascii text converter with various other output options."),
    keywords = "Ascii, Image",
    url = "https://github.com/jaschon/im2a-py",
    packages=['im2a', 'bin', 'tests'],
    long_description=read('README.md'),
    install_requires=read('requirements.txt').splitlines(),
    scripts=['bin/im2a',],
)
