# Here to trigger an error
import pytest

# Doing this to be a little sneaky, at least
from A_defining_strings import your_first_name, your_last_name
cap = your_last_name.upper()

def test_name_methods(capsys):
    # Again being a bit funny to grab the print...
    import B_string_methods as B
    assert B.cap_last_name == cap
    assert B.name_len == len(B.cap_last_name) + len(B.your_first_name) + 1
    out, err = capsys.readouterr()
    last_line = out.split('\n')[-2]
    words = last_line.split(', ')
    assert words[0:1] == [B.cap_last_name]
    assert words[1:2] == [B.your_first_name]

