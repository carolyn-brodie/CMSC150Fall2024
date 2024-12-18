import doctest


def add(a, b):
    """
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> add(2, 3)
    5
    >>> add(2, 2)
    4
    """
    return a * b

doctest.testmod(verbose=True)