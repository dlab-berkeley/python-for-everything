import pytest

def test_simple(capsys):
    import A_lists as A
    assert len(A.my_list) == 0


def test_your_list(capsys):
    import A_lists as A
    assert len(A.your_list) == 3, "List must have 3 items"
    assert type(A.your_list[0]) is str,  "Your name must be a string"
    assert type(A.your_list[1]) is int,  "Your age must be an integer"
    assert type(A.your_list[2]) is str,  "Your color must be a string"
