# Here to trigger an error
import pytest

def test_can_drink(capsys):
    # Again being a bit funny to grab the print...
    import A_checking_the_right_thing as A
    out, _ = capsys.readouterr()

    # Here we're being flexible in allowing where folks can print things
    lines = out.split('\n')
    try:
        loc = lines.index("Checking Alice")
    except ValueError:
        loc = -1
    assert loc >= 0, 'Should print "Checking Alice"'
    # Having found our Alice line, we make sure the next line is correct
    assert lines[loc+1] == "This isn't right!", \
            'Should print "This isn\'t right!" for Alice'

    # Bob is easy...
    assert "Checking Bob" not in lines

    # And checking Charles is again like Alice
    try:
        loc = lines.index("Checking Charles")
    except ValueError:
        loc = -1
    assert loc >= 0, 'Should print "Checking Charles"'
    assert lines[loc+1] == "OK!", \
             'Should print "OK!" for Charles'
