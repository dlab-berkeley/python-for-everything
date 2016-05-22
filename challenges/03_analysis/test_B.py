#!/bin/env python

import os
import pandas as pd
import pytest

import B_tables as B

def test_import():
    assert isinstance(B.person_data, pd.DataFrame)
    assert B.person_data.shape == (100,3)

def test_merge():
    assert B.all_data.shape == (103,5)

def test_new():
    assert os.path.isfile('../../data/height_above_sea.csv')
    data = pd.read_csv('../../data/height_above_sea.csv')
    assert len(data) in [100, 103]
    assert "height_above_sea" in data
