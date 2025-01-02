from calculator import Calculator


def test_add_one():
    calc = Calculator()
    calc.set(1)
    calc.add()
    assert calc.total == 1


def test_initial():
    calc = Calculator()
    assert calc.total == 0


def test_sub_one():
    calc = Calculator()
    calc.set(1)
    calc.sub()
    assert calc.total == -1


def test_add_one_add_one():
    calc = Calculator()
    calc.set(1)
    calc.add()
    calc.set(1)
    calc.add()
    assert calc.total == 2
