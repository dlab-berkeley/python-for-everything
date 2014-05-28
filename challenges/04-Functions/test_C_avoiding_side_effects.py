import pytest

def test_exponentiate(capsys):
    # This is the last time, I swear!
    import C_avoiding_side_effects as C
    assert C.exponentiate(2,10) == 1024def test_exponentiate(capsys):
    out, _ = capsys.readouterr()
    assert out == ''

