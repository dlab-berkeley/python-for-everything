#!/bin/env python

import json
import os
import pytest

import B_stemming as B

def test_get_tokens():
    assert len(B.get_tokens("Hey, this isn't a test!")) >= 6

def test_get_stems():
    assert B.get_stems(['tries', 'fanned', 'runs']) == ['tri', 'fan', 'run']

def test_stop_words():
    with open('../../data/04_text.md', 'r') as f:
        document = f.read()
    stopwords = B.get_stopwords(B.get_stems(B.get_tokens(document)))
    assert len(stopwords) == 10
    for word in ['for', 'the', '#', 'http', '[', ']', '-', ':', '(', ')']:
        assert word in stopwords

def test_remove_stopwords():
    document = "The man bought Alice in Wonderland, a book for children, but which is really for the mathematically inclined adult".split()
    stopwords = ["the", "and", "for"]
    assert len(B.remove_stopwords(stopwords, document)) == 15
