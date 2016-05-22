#!/bin/env python

import pytest
import re

import A_re as A

def test_pattern():
    assert re.search(A.P_URL, 'http://www.npr.org')
    assert not re.search(A.P_URL, 'Mr.DillonNiederhut')

def test_function():
    with open('../../data/03_text.md', 'r') as f:
        d = f.read()
    r = A.get_urls(d)
    assert len(r) == 28
    assert r[0] == 'https://github.com'
