import B_data_and_variables as B

def test_instructors():
    assert 'Dav' in B.instructors
    assert 'Rochelle' in B.instructors
    assert 'Dave' not in B.instructors

def test_types():
    assert type(B.some_int) is int
    assert type(B.some_float) is float
    assert type(B.some_bool) is bool

def test_reassignment():
    assert B.my_lucky_number == 9
