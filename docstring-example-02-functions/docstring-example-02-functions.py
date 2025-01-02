""" A module to calculate factorial

>>> factorial(5)
120
"""


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
    """
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result
