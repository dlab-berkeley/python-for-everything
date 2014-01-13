import B_data_and_variables as B

def test_instructors():
    assert 'Dav' in B.instructors
    assert 'Rochelle' in B.instructors
    assert 'Dave' not in B.instructors

def test_types():
    assert type(B.some_int) == int
    assert type(B.some_float) == float
    assert type(B.some_bool) == bool

def test_reassignment():
    assert B.my_lucky_number == 9
