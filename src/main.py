from functions import *

def main():
    try:
        seq = str(input("Enter a DNA sequence: "))
        if (validate_seq(seq)) == False:
            raise InvalidSequenceError
        print("Reverse: "+ reverse_seq(seq))
    except InvalidSequenceError:
        print("Invalid DNA sequence, please try again")
        main()

main()