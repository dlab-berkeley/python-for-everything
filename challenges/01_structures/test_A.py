import pytest

import A_list as A


def test_count_ones():
    assert A.list_count_ones() == 2

def test_mean():
    assert A.list_mean() == 3.5

def test_lt3():
    assert A.list_lt3() == 4
