# Here to trigger an error
import pytest

def test_names(capsys):
    # Again being a bit funny to grab the print...
    import A_defining_strings as A
    assert type(A.your_first_name) is str
    assert type(A.your_last_name) is str
    out, err = capsys.readouterr()
    assert 'The second letter of my last name is ' + A.your_last_name[1] in out
