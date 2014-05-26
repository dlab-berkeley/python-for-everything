# A simple test to illustrate if __name__ == '__main__'

import B_script_conventions as B

def test_module_var():
    assert B.module_var == "I am totally defined"
