# This is just here so this breaks if you don't have pytest (which makes more
# sense than missing capsys below)
import pytest

def test_printing(capsys):
    # This is a little unorthodox, but we're doing Test-driven *learning*
    # Folks don't know about functions yet!
    import A_print_stuff
    out, err = capsys.readouterr()
    assert out == "Hello Python!\n"
