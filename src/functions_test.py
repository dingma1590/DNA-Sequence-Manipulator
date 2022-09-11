from functions import *
from termcolor import colored

def test_validate():
    assert validate_seq("") == False
    assert validate_seq("ACTTAGGATTTTACTTCACC") == True
    assert validate_seq("acttaggattttacttcacc") == True
    assert validate_seq("ABCDEFG") == False
    assert validate_seq("acttaggatzttact") == False

def test_reverse():
    assert reverse_seq("ACTTAGGATTTTACTTCACC") == "CCACTTCATTTTAGGATTCA"
    assert reverse_seq("cgatagcatt") == "TTACGATAGC"

def test_complement():
    assert complement_seq("ACTTAGGATTTTACTTCACC") == "TGAATCCTAAAATGAAGTGG"
    assert complement_seq("tcagtggtatcacct") == "AGTCACCATAGTGGA"

def test_rev_comp():
    assert rev_comp_seq("ACTTAGGATTTTACTTCACC") == "GGTGAAGTAAAATCCTAAGT"
    assert rev_comp_seq("tcagtggtatcacct") == "AGGTGATACCACTGA"

def test_t_to_u():
    assert thymine_uracil("ACTTAGGATTTTACTTCACC") == "ACUUAGGAUUUUACUUCACC"
    assert thymine_uracil("tcagtggtatcacct") == "UCAGUGGUAUCACCU"

def test_transcribe():
    assert transcribe_seq("ACTTAGGATTTTACTTCACC", 1) == "UGAAUCCUAAAAUGAAGUGG"
    assert transcribe_seq("tcagtggtatcacct", 1) == "AGUCACCAUAGUGGA"
    assert transcribe_seq("ACTTAGGATTTTACTTCACC", 0) == "ACUUAGGAUUUUACUUCACC"
    assert transcribe_seq("tcagtggtatcacct", 0) == "UCAGUGGUAUCACCU"

def test_tran_helper():
    assert translate_helper("AGUCACCAUAGUGGA") == "SHHSG"
    assert translate_helper("UCAGUGGUAUCACCUUGAAUCCUAAAAUGAAGUGGC") == "SVVSP_ILK_SG"

def test_translate():
    assert translate_seq("ACTTAGGATTTTACTTCACC", 0, 0) == " T_DFTS CC"
    assert translate_seq("ACTTAGGATTTTACTTCACC", 0, 1) == "A LRILLH C"
    assert translate_seq("ACTTAGGATTTTACTTCACC", 0, 2) == "AC LGFYFT "
    assert translate_seq("tcagtggtatcacct", 1, 0) == " SHHSG "
    assert translate_seq("tcagtggtatcacct", 1, 1) == "A VTIV GA"
    assert translate_seq("tcagtggtatcacct", 1, 2) == "AG SP_W A"

def test_rf():
    assert seq_reading_frame("ATGCAATGGGGAAATGTTACCAGGTCCGAACTTATTGAGGTAAGACAGATTTAA", 0, 0) == \
        " "+colored("ATG", "green")+" CAA TGG GGA AAT GTT ACC AGG TCC GAA CTT ATT GAG GTA AGA CAG ATT "+colored("TAA", "red")+" "
    assert seq_reading_frame("atgcaatggggaaatgttaccaggtccgaacttattgaggtaagacagatttaa", 0, 1) == \
        "A TGC AAT GGG GAA "+colored("ATG", "green")+" TTA CCA GGT CCG AAC TTA TTG AGG "+colored("TAA", "red")+" GAC AGA TTT AA"
    assert seq_reading_frame("ATGCAATGGGGAAATGTTACCAGGTCCGAACTTATTGAGGTAAGACAGATTTAA", 0, 2) == \
        "AT GCA "+colored("ATG", "green")+" GGG AAA TGT TAC CAG GTC CGA ACT TAT "+colored("TGA", "red")+" GGT AAG ACA GAT TTA A"