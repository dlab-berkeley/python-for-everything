#!/bin/env python

import pytest
import re

import B_html as B

def test_page():
    page = B.get_page()
    assert page.ok
    assert 'http://www.whattimeisit.com/' in page.url

def test_time():
    page = B.get_page()
    time = B.get_time(page)
    assert isinstance(time, str)
    assert re.search(r'[0-9]+:[0-9]+', time)
