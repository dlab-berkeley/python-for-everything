#!/bin/env python

import json
import pytest

import A_json as A

def test_search():
    with open('../../data/03_tweet.json', 'r') as f:
        tweet = json.load(f)
    assert A.search(tweet, 'name') == ['Yelekreb Bald']
    assert A.search(tweet, 'entities') == [
        {'hashtags': [], 'symbols': [], 'urls': [], 'user_mentions': []},
        {'description': {'urls': []}}]
    assert A.search(tweet, 'geo') == [None]
