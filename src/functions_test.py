from functions import *

def test_validate():
    assert validate_seq("") == False
    assert validate_seq("ACTTAGGATTTTACTTCACC") == True
    assert validate_seq("acttaggattttacttcacc") == True
    assert validate_seq("ABCDEFG") == False
    assert validate_seq("acttaggatzttact") == False

def test_reverse():
    assert reverse_seq("ACTTAGGATTTTACTTCACC") == "CCACTTCATTTTAGGATTCA"
    assert reverse_seq("cgatagcatt") == "ttacgatagc"