# Here to trigger an error
import pytest


def test_name_methods(capsys):
    # Again being a bit funny to grab the print...
    import C_interpolation
    out, err = capsys.readouterr()
    lines = out.split('\n')
    assert 'this string is 33 characters long' == lines[0]
    assert '1.02' in lines[1]
    assert '3.0' not in lines[1]
    assert '3.0' in lines[2]
    assert '1.02' not in lines[2]


