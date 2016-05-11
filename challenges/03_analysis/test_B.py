#!/bin/env python

import os
import pandas as pd
import pytest

import C_tables as C

def test_import():
    assert isinstance(C.person_data, pd.DataFrame)
    assert C.person_data.shape == (100,3)

def test_merge():
    assert C.all_data.shape == (103,6)

def test_new():
    assert os.path.isfile('../../data/height_above_sea.csv')
    data = pd.read_csv('../../data/height_above_sea.csv')
    assert len(data) == 100
    assert "height_above_sea" in data
