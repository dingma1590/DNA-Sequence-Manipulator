from main import *

def test_validate():
    assert validate_sequence("") == False
    assert validate_sequence("ACTTAGGATTTTACTTCACC") == True
    assert validate_sequence("acttaggattttacttcacc") == True