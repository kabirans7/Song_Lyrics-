#Assignment 1: Practice with Dictionaries, Tuples and Lists 
#Question 2 

import pytest 
from typing import List, Tuple, Dict, Optional


#Opening and reading the file
def get_file():
    try:
        with open("pi_million_digits.txt", "r") as f:
            contents = f.read()
            return contents 
    except FileNotFoundError as e:
        print("file not found")


#Calculating the frequency of each digit (0 through 9)
def create_digit_count(contents):
    digit_count = {}
    for i in contents: 
        digit_count[i] = digit_count.get(i, 0) + 1

    #Deleting new lines and empty spaces
    del digit_count["\n"]
    del digit_count[" "]

    #Sorting 0-9 in order
    digit_count = dict(sorted(digit_count.items()))
    return digit_count

def produce_frequency(digit_count):
    print(f"Frequency of digits in the first million digits of π:")
    for key, value in digit_count.items():
        print(f"{key}: {value}")



#Search Feature for user input
def get_sequence(sequence, contents):
    return contents.find(sequence)
    print(f"The sequence {sequence} was found at position {contents.find(sequence)}")


#Removing all occurrences of 8 and updating to new file
def remove_eights():
    contents = contents.replace("8", "")
    with open("pi_million_digits_no_8.txt", "w") as f:
        f.write(contents)


#To help reference the test_cases.py for unit testing
if __name__ == "__main__":
    contents = get_file()
    digit_count = create_digit_count(contents)
    produce_frequency(digit_count)
    sequence = input("Enter a sequence of digits to search (up to 6 digits): ")
    get_sequence(sequence, contents)