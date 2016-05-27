#!/bin/env python

import json
import os
import pytest

import B_stemming as B

def test_token():
    truth = hasattr(B, 'nltk') + hasattr(B, 'word_tokenize') + hasattr(B, 'wordpunct_tokenize')
    assert truth > 0
    assert len(B.token_list) >= 400

def test_stemmer():
    fp = '../../data/stemmed_document.json'
    assert os.path.isfile(fp)
    with open(fp, 'r') as f:
        d = json.load(f)
    assert len(d) == len(B.token_list)
    for unstemmed_word in ['fundamentals', 'discover', 'very', 'secure']:
        assert unstemmed_word not in d

def test_stop_words():
    assert type(B.stop_list) is list
    assert len(B.stop_list) == 10
