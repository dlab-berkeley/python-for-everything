# This first example lifted from http://pytest.org/latest/getting-started.html
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
