#Referencing pi.py file and importing functions get_sequence, get_file, create_digit_count
from pi import get_sequence, get_file, create_digit_count


#Testing if first 6 numbers in pi, return a position of 0
contents = get_file()
def test_get_sequence():
    assert get_sequence("314159", contents) == 0


#Testing the digit count 
def test_create_digit_count():
    assert isinstance(create_digit_count(contents), dict)