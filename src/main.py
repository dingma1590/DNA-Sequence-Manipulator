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

def main():
    try:
        seq = str(input("Enter a DNA sequence: "))
        if (validate_seq(seq)) == False:
            raise InvalidSequenceError
        print("Reverse: "+ reverse_seq(seq))
    except InvalidSequenceError:
        print("Invalid DNA sequence, please try again")
        main()

# main()