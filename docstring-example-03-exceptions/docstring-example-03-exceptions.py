""" A module to calculate factorial

>>> factorial(5)
120
"""

import math


def factorial(n):
    """Calculates the factorial of n.

    Args:
        n (int)

    Returns:
        results (int): the factorial of `n`

    >>> [factorial(i) for i in range(1, 6)]
    [1, 2, 6, 24, 120]

    >>> factorial(30)
    265252859812191058636308480000000

    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be positive

    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer

    >>> factorial(30.0)
    265252859812191058636308480000000

    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    if n <= 0:
        raise ValueError("n must be positive")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result
