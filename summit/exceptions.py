__author__ = 'Greg'


class InvalidOperator(ValueError):
    """
    Raised when a operator is provided that is not a member of the allowed set of operators
    """


class NotEnoughChildren(ValueError):
    """
    Raised when less than two children were provided, stopping the operation chain from completing.
    """


class RealNumberExpected(ValueError):
    """
    Raised when a child is expected to be a real number but a different type of object/value was provided.
    """