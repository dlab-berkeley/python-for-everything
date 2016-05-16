#!/bin/env python

import json
import pytest

import A_json as A

def test_load():
    with open('../../data/02_tweet.json', 'r') as f:
        test_data = json.load(f)
    assert A.tweet == test_data

def test_entity_getter():
    test_data = list(A.entity_getter(A.tweet))
    assert {'description': {'urls': []}} in test_data
    assert {'hashtags': [], 'symbols': [], 'urls': [], 'user_mentions': []} in test_data
