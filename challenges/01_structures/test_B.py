#!/bin/env python

import pytest

import B_dict as B


def test_unique_values():
    assert B.unique_values({}) == 0
    assert B.unique_values({'one' : 1}) == 1
    assert B.unique_values({'one' : 1, 'two' : 1}) == 1

def test_key_check():
    assert B.dict_key_check('dlab', {'dlab' : 1, 'bids' : 1})
    assert B.dict_key_check('Ca', {'fl' : 1, 'ca' : 1})
    assert not B.dict_key_check('R', {'python' : 1, 'scala' : 0})
