class TreeManipulationError(Exception):
    """
    Base class for tree manipulation exceptions
    """
    pass


class InvalidInput(TreeManipulationError):
    """
    Exceptions raised for invalid input
    """
    pass


class ParseError(TreeManipulationError):
    """
    Exceptions rasied for parsing tree node
    """
    pass


class EvaluationError(TreeManipulationError):
    """
    Exceptions raised for tree traversal and evaluation
    """
    pass

