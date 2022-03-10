# define an exception
class NotNumberError(Exception):
    pass

class Calculator:
    def __init__(self):
        self.current = 0
        self.total = 0

    def set(self, value):
        # if value is not a number (int or float) raise a NotNumberException
        if not (isinstance(value, int) or isinstance(value, float)):
            raise NotNumberError(f"the given {value} is not a number")
        self.current = value

    def add(self):
        self.total += self.current

    def sub(self):
        self.total -= self.current

    def total(self):
        return self.total
