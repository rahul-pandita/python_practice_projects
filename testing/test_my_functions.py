import pytest
import my_functions

def test_add():
    assert my_functions.add(2, 3) == 5
    # assert my_functions.add(2, 2) == 5

def test_divide():
    assert my_functions.divide(4, 2) == 2

def test_divide_zero():
    # Expecting a division error when we call the divide function
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)