import pytest

def test_exponentiate(capsys):
    # This is the last time, I swear!
    import B_avoiding_side_effects as B
    assert B.exponentiate(2,10) == 1024
    out, _ = capsys.readouterr()
    assert out == ''

