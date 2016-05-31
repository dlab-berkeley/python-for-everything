#!/bin/env python

import pytest

import C_loops as C

def test_list_to_dict():
    assert C.list_to_dict([]) == {}
    assert 1 in C.list_to_dict([1])
    assert 'juan' in C.list_to_dict(['juan', 'dillon'])

def test_print_while(capfd):
    C.print_while()
    out, err = capfd.readouterr()
    assert out == 'b\ne\nr\nk\ne\nl\ne\ny\n'
