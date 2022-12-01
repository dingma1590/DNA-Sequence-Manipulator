from exceptions import *
from termcolor import colored

genetic_code = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                 
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
    'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
    }


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
        result += seq[index - s].upper()

    return result


def complement_seq(seq: str) -> str:
    """
    Returns the complement of the given sequence

    The complement of a DNA sequence replaces every occurence of A with T and C with G, vice versa.
    """
    result = ""
    for s in range(len(seq)):
        if seq[s].casefold() == "a":
            result += "T"
        elif seq[s].casefold() == "t":
            result += "A"
        elif seq[s].casefold() == "c":
            result += "G"
        elif seq[s].casefold() == "g":
            result += "C"
    
    return result 


def rev_comp_seq(seq: str) -> str:
    """
    Returns the reverse complement of the given sequence
    """
    return complement_seq(reverse_seq(seq))


def thymine_uracil(seq: str) -> str:
    """
    Returns the sequence with every occurence of T replaced with U
    """
    result = ""

    for s in range(len(seq)):
        if seq[s].casefold() == "t":
            result += "U"
        else:
            result += seq[s]
    
    return result.upper() 


def transcribe_seq(seq: str, mode: int) -> str:
    """
    Returns the transcribed RNA seqeuence of the given DNA sequence

    If mode = 0: assume seq is the coding strand (sense); replace every occurence of T with U

    If mode = 1: assume seq is the template strand (antisense); complement then replace every occurence
    of T with U
    """
    if mode == 0:
        return thymine_uracil(seq)
    if mode == 1:
        return thymine_uracil(complement_seq(seq))


def translate_helper(seq: str) -> str:
    """
    Returns the given sequence translated according to the genetic code, each letter represents one amino acid.

    "_" represents a stop codon
    """
    result = ""
    codon_temp = ""
    for s in seq:
        codon_temp += s
        if len(codon_temp) == 3:
            result += genetic_code[codon_temp.upper()]
            codon_temp = ""

    return result


def translate_seq(seq: str, mode: int, offset: int) -> str:
    """
    Returns the given sequence translated according to the genetic code, each letter represents one amino acid.

    This function ignores and appends to result the first 0-2 nucleotides (indicated by offset), and any 
    remaining nucleotides.
 
    "_" represents a stop codon
    """

    pre = seq[:offset]
    post = seq[len(seq)-len(seq[offset:])%3:]
    mod_seq = seq[offset:len(seq)-len(seq[offset:])%3]

    result = ""

    if mode == 0:
        result = transcribe_seq(pre, mode).upper() + " " + translate_helper(transcribe_seq(mod_seq, mode)) + \
            " " + transcribe_seq(post, mode).upper()
    elif mode == 1:
        result = transcribe_seq(pre, mode).upper() + " " + translate_helper(transcribe_seq(mod_seq, mode)) + \
            " " + transcribe_seq(post, mode).upper()
    
    return result


def seq_reading_frame(seq: str, mode: int, offset: int) -> str:
    """
    Returns the reading frame of the given sequence with offset, highlights any start/stop codons

    Extra nucleotides are appended to the beginning/end of the result, a space is inserted between each codon
    """
    if mode == 1:
        seq = complement_seq(seq)

    pre = seq[:offset]
    post = seq[len(seq)-len(seq[offset:])%3:]
    mod_seq = seq[offset:len(seq)-len(seq[offset:])%3].upper()

    result = ""
    codon_temp = ""

    for s in mod_seq:
        codon_temp += s
        if len(codon_temp) == 3:
            if codon_temp == "ATG":
                codon_temp = colored(codon_temp, "green")
            elif codon_temp in {"TAA", "TGA", "TAG"}:
                codon_temp = colored(codon_temp, "red")
            result += codon_temp + " "
            codon_temp = ""

    return pre.upper() + " " + result + post.upper()