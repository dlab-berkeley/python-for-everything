#!/bin/env python

import pytest

import A_list as A

def test_arthur():
    assert A.prepend_arthur([0]) == ["In the name of Arthur of the House Pendragon, the first of his name, King of the Britons, Defeater of the Saxons, and Sovereign of all England:", 0]
    assert A.prepend_arthur([]) == ["In the name of Arthur of the House Pendragon, the first of his name, King of the Britons, Defeater of the Saxons, and Sovereign of all England:"]

def test_half():
    assert A.get_second_half([1,2,3]) == [2,3]
    assert A.get_second_half([]) == []

def test_mean():
    assert A.get_mean([-1,0,1]) == 0
    assert A.get_mean([0,0,0]) == 0
