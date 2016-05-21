#!/bin/env python

import pytest

import B_html as B

def test_page():
    page = B.page
    assert page.ok
    assert page.url == 'https://isitchristmas.com/'
    assert 'Built by Eric Mill' in page.text

def test_text():
    assert B.title in [
    'Is it Christmas?',
    '<title>Is it Christmas?</title>',
    ]
    assert not B.text

def test_header():
    assert len(B.header) == 90
