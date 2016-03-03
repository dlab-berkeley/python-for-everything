import pytest

import C_loops as C


def test_print_while(capfd):
    C.print_while()
    out, err = capfd.readouterr()
    assert out == 'b\ne\nr\nk\ne\nl\ne\ny\n'
