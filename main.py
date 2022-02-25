import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
import re
from collections import Counter
from tqdm import tqdm 
from pyod.models.copod import COPOD

def read_word_list(file_name:str): 
    result = []
    with open(file_name) as fp:
      result.extend([word.strip() for word in fp.readlines()])
    return result
  
# Read in word lists
possible_word_list = read_word_list("possible_answers.txt")
accepted_words_list = read_word_list("accepted_words.txt")

# create a letter occurence dictionary
words_string = ''.join(accepted_words_list)
letter_counts = dict(Counter(words_string))

# create a letter frequency dictionary
letter_frequencies = {k:v/len(accepted_words_list) for k, v in 
                      letter_counts.items()}
# create letter frequency DataFrame
letter_frequencies = 
pd.DataFrame({'Letter':list(letter_frequencies.keys()), 'Frequency' : list(letter_frequencies.values())}).sort_values('Frequency', ascending=False)

