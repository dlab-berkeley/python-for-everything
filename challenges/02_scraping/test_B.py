#!/bin/env python

import pytest

import A_html as A

def test_page():
    page = A.page
    assert page.ok
    assert page.url == 'https://isitchristmas.com/'
    assert 'Built by Eric Mill' in page.text

def test_text():
    assert A.title in [
    'Is it Christmas?',
    '<title>Is it Christmas?</title>',
    ]
    assert not A.text

def test_header():
    assert len(A.header) == 90
