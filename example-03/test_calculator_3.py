import pytest
from calculator import Calculator


# define fixtures
@pytest.fixture
def calculator():
    """Returns a Calculator instance"""
    return Calculator()


def test_add_one(calculator):
    calculator.set(1)
    calculator.add()
    assert calculator.total == 1


def test_initial(calculator):
    assert calculator.total == 0


def test_sub_one(calculator):
    calculator.set(1)
    calculator.sub()
    assert calculator.total == -1


def test_add_one_add_one(calculator):
    calculator.set(1)
    calculator.add()
    calculator.set(1)
    calculator.add()
    assert calculator.total == 2
