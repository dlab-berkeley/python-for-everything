import pytest

import B_dict as B


def test_dict_unique_values():
    assert B.dict_unique_values() == 4

def test_dict_make_it_nested():
    e = B.dict_make_it_nested()
    assert 'deep' in e['two']

def test_dict_key_check():
    assert B.dict_key_check('dlab', {'dlab' : 1, 'bids' : 1}) is True
    assert B.dict_key_check('Ca', {'fl' : 1, 'ca' : 1}) is True
    assert B.dict_key_check('R', {'python' : 1, 'scala' : 0}) is False
