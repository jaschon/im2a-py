#!/usr/bin/env python3

import os
from setuptools import setup
import im2a

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "im2a",
    version = im2a.__version__,
    author = im2a.__author__,
    description = (im2a.__doc__,),
    keywords = "Ascii, Image",
    url = "https://github.com/jaschon/im2a-py",
    packages=['im2a', 'bin', 'tests'],
    long_description=read('README.md'),
    install_requires=read('requirements.txt').splitlines(),
    scripts=['bin/im2a',],
)
