#!/bin/env python

import json
import pytest

import C_json as C

def test_load():
    with open('../../data/02_tweet.json', 'r') as f:
        test_data = json.load(f)
    assert C.tweet == test_data

def test_entity_getter():
    test_data = list(C.entity_getter(C.tweet))
    assert {'description': {'urls': []}} in test_data
    assert {'hashtags': [], 'symbols': [], 'urls': [], 'user_mentions': []} in test_data
