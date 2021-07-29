import pytest
import calculator as calc
from calculator import Calculator

# define fixtures
@pytest.fixture
def calculator():
    """Returns a Calculator instance"""
    return Calculator()

def test_initial(calculator):
    assert calculator.total == 0

# test for NotNumberError
def test_NotNumberError(calculator):
    with pytest.raises(calc.NotNumberError):
        calculator.set("a string")

@pytest.mark.parametrize(
    'input_1,expected',
    [
        (0, 0),
        (1, 1),
        (2, 2),
    ]
)
def test_add_one(calculator, input_1, expected):
    calculator.set(input_1)
    calculator.add()
    assert calculator.total == expected

def test_sub_one(calculator):
    calculator.set(1)
    calculator.sub()
    assert calculator.total == -1

@pytest.mark.parametrize(
    'input_1, input_2, expected',
    [
        (0, 1, 1),
        (2, 5, 7),
        (10, 1, 11),
    ]
)
def test_add_one_add_one(calculator, input_1, input_2, expected):
    calculator.set(input_1)
    calculator.add()
    calculator.set(input_2)
    calculator.add()
    assert calculator.total == expected
