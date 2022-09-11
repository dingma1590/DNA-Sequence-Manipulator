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

class InvalidModeError(Error):
    """
    Raised when the given move is invalid
    """
    pass

class InvalidOffsetError(Error):
    """
    Raised when the given offset is invalid
    """
    pass