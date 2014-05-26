import A_checking_again as A

def test_can_drink():
    '''This is a much clearer test now that we're using functions!'''
    assert A.can_drink(21) == True
    assert A.can_drink(22) == True
    assert A.can_drink(20) == False

def test_enforce(capsys):
    '''Notice that we're not restricted to the data in our script.'''
    A.enforce("John", 18, False)
    A.enforce("Chuck", 18, True)
    A.enforce("Bob", 21, True)
    # Since we specify the operations more tightly, we can be more precise in
    # what specific lines should be in our test
    out, _ = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == "Checking Chuck!"
    assert lines[1] == "This isn't right!"
    assert lines[2] == "Checking Bob!"
    assert lines[3] == "OK!"
    assert lines[4] == ""

# Advanced users should note that the above tests could be made even more
# efficient using the "parametrize" decorator from pytest!
