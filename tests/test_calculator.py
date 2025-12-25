import pygittest
from src.calculator import add, subtract, multiply, divide


def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(5, 0) == 5



def test_subtract_positive():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(-2, 3) == -5

def test_subtract_zero():
    assert subtract(7, 0) == 7


def test_multiply_positive():
    assert multiply(4, 5) == 20

def test_multiply_negative():
    assert multiply(-3, 2) == -6


def test_divide_positive():
    assert divide(10, 2) == 5.0

def test_divide_negative():
    assert divide(-6, 3) == -2.0

def test_divide_fraction():
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Деление на ноль запрещено"):
        divide(1, 0)