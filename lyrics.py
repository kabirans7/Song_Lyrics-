#Assignment 1: Practice with Dictionaries, Tuples and Lists 
#Question 1 

import pytest
from typing import List, Tuple, Dict, Optional

#Step 1: Read and store lyrics
#Open and read the song lyrics from a file
#Splitting the lyrics and making them lower case

with open("lyrics.txt", "r") as f:
    content = f.read().lower().split("\n")


#Removing punctuation and special characters

words_list = []
for i in content:
    for j in r"!@#$%^&*()-_=+\|[]{};:/?.>,'":
        i = i.replace(j, "")
    for j in i.split(" "):
        words_list.append(j)


#Step2: Word Frequency Analysis
#Using a dictionary to count word frequency

word_count = {}
for i in words_list:
    word_count[i] = words_list.count(i)
    

#Using tuples to store word frequency pairs
def sort_tuples(x):
    return x[1]


word_pairs = []
for key, value in word_count.items():
    word_pairs.append((key, value))

word_pairs.sort(key=sort_tuples)


#Step3: Analysis
#Total Number of Words in the song
total_words = len(words_list)
print(f"Total Word Count:", total_words)

#Number of unique words used in the song
unique_words = len(set(words_list))
print(f"Number of Unique Words:", unique_words)


title = "Top 5 Most Common Words:"
print(title)
#Top 5 most common words and counts
for i in word_pairs[-5:]:
    print (f"{i[0]}: {i[1]}")


#Longest word in lyrics
def get_longest(x):
    return len(x[0])

word_pairs.sort(key=get_longest)
print(f"Longest Word:", word_pairs[-1][0])

