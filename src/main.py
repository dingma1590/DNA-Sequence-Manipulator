from functions import *

def main():
    try:
        seq = str(input("Enter a DNA sequence (Note: Results are always shown 5' to 3'): "))
        mode = int(input("Enter 0 if this is a coding strand (5' to 3'), 1 if it's a template strand (3' to 5'): "))
        offset = int(input("Enter the offset (0-2) for translation/reading frame functionalities: "))
        if (validate_seq(seq)) == False:
            raise InvalidSequenceError
        if mode != 0 and mode != 1:
            raise InvalidModeError
        if offset != 0 and offset != 1 and offset != 2:
            raise InvalidOffsetError
        print("=============================================================================================")
        print(colored("Original Sequence: ", attrs=['bold']) + seq)
        print()
        print(colored("Reverse: ", attrs=['bold']) + reverse_seq(seq))
        print()
        print(colored("Complement: ", attrs=['bold']) + complement_seq(seq))
        print()
        print(colored("Reverse Complement: ", attrs=['bold']) + rev_comp_seq(seq))
        print()
        print(colored("Transcribed RNA Sequence: ", attrs=['bold']) + transcribe_seq(seq, mode))
        print()
        print(colored("Reverse Amino Acid Sequence: ", attrs=['bold']) + translate_seq(seq, mode, offset))
        print()
        print(colored("Reading Frame: ", attrs=['bold']) + seq_reading_frame(seq, mode, offset))
        print("=============================================================================================")
    except InvalidSequenceError:
        print("Invalid DNA sequence, please try again.")
        main()
    except InvalidModeError:
        print("Invalid mode, please enter 0 for coding strand and 1 for template strand.")
        main()
    except InvalidOffsetError:
        print("Invalid offset, please enter an offset value between 0 and 2, inclusive.")
        main()

main()