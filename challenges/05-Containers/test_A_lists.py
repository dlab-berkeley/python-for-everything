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

def test_spam(capsys):
    import A_lists as A

    empty_list = []
    result = A.add_spam(empty_list)
    assert len(result) == 1, "add_spam([]) does not return a list of length 1"
    assert result[0] == 'spam', "add_spam([]) does not add 'spam'"
    
    test_list = ['here', 'is', 22, 'a', 'list']
    old_length = len(test_list)
    result = A.add_spam(test_list)
    assert len(result) == old_length+1, "add_spam() does not add an item"
    assert result[-1] == 'spam', "add_spam() does not add 'spam' to the end"
