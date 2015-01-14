import pytest

def test_simple():
    import C_dicts as C
    assert len(C.people) > 0, "people should contain something"
    for key, value in C.people.items():
        assert isinstance(key, str), "Keys should be strings"
        assert isinstance(value, int), "Values should be integers"

def test_age_next_birthday():
    import C_dicts as C
    name, age = C.people.items()[0]
    assert C.age_next_birthday(name) == age + 1
    assert C.age_next_birthday('nobodyscalledthis') == -1
