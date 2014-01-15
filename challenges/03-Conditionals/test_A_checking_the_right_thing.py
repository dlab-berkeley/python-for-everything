# Here to trigger an error
import pytest

# Doing this to be a little sneaky, at least

def test_can_drink(capsys):
    # Again being a bit funny to grab the print...
    import A_checking_the_right_thing as A
    assert A.sally_can_drink == False # Using == False to get clearer errors!
    assert A.john_can_drink == True
    out, _ = capsys.readouterr()
    print out
    lines = out.split('\n')
    assert lines[0] == "Checking Alice"
    assert lines[1] == "This isn't right!"
    assert lines[2] == "Checking Bob"
    assert lines[3] == "OK!"
    assert lines[4] != "Checking Charles"

