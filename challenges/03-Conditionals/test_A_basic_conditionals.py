# Here to trigger an error
import pytest

import A_basic_conditionals as A

def test_can_drink(capsys):
    # Again being a bit funny to grab the print...
    assert A.sally_can_drink == False # Using == False to get clearer errors!
    assert A.john_can_drink == True
