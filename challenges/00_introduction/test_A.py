#!/bin/env python

import pytest
import sys

import A_objects as A

def test_version():
    assert A.version > (3,4)

def test_dillon():
    assert isinstance(A.dillon, float)
