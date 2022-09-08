from exceptions import *

def validate_seq(seq: str) -> bool:
    """Returns true if seq is a valid DNA sequence, false otherwise
    
    A DNA sequence is valid if it contains only the letters A, C, G and T
    """
    if seq == "":
        return False

    for s in seq:
        # if not(s.casefold() == "a" or s.casefold() == "c" or s.casefold() == "g" or s.casefold() == "t"):
        #     return False
        # else:
        #     pass
        if not (s.casefold() in {"a", "c", "g", "t"}):
            return False
        else:
            pass

    return True


def reverse_seq(seq: str) -> str:
    """
    Returns the reverse of the given sequence
    """
    result = ""
    index = -1
    for s in range(len(seq)):
        result += seq[index - s]

    return result


def complement_seq(seq: str) -> str:
    """
    Returns the complement of the given sequence

    The complement of a DNA sequence replaces every occurence of A with T and C with G, vice versa.
    """
    result = ""
    for s in range(len(seq)):
        if seq[s].casefold() == "a":
            result += "t"
    
    return result 