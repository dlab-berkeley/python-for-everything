import inspect
import pytest

import B_syntax as B

def test_numbers():
    assert isinstance(B.counting_numbers, str)
    assert 'three' in B.counting_numbers

def test_arthur():
    assert inspect.signature(B.arthurify).parameters
    assert B.arthurify('three four') == 'five four'
