#!/bin/env python

import pytest
import re

import A_re as A

def test_read():
    fp = '../../data/04_text.md'
    with open(fp, 'r') as f:
        d = f.read()
    assert A.read_file(fp) == d

def test_get_url():
    with pytest.raises(ValueError):
        A.get_url_list(12)
    assert A.get_url_list('http://www.npr.org/sections/thesalt/2016/01/01/461704287/vegetables-likely-to-take-more-of-your-plate-in-2016')
    assert A.get_url_list("https://twitter.com/search?q=%23mozsprint&src=typd")
    assert not A.get_url_list('Mr.DillonNiederhut')

def test_process():
    fp1 = '../../data/04_text.md'
    fp2 = '../../README.md'
    r = A.process_files(fp1, fp2)
    assert len(r) == 2
    assert len(r[fp1]) == 28
    assert 'github.com' in r[fp1][0]
