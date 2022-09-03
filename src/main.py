
def validate_sequence(seq: str) -> bool:
    """Return true if seq is a valid DNA sequence, false otherwise
    
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