class Error(Exception):
    """
    Base class for exceptions
    """
    pass

class InvalidSequenceError(Error):
    """
    Raised when the given DNA sequence is invalid 
    """
    pass