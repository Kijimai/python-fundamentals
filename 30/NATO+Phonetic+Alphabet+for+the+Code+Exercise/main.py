# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


# answered = False
# while not answered:
#   word = input("Enter a word: ").upper()
#   try:
#       output_list = [phonetic_dict[letter] for letter in word]
#   except KeyError:
#       print("Sorry, Only letters in the alphabet please.")
#   else:
#       print(output_list)
#       answered = True

# Recursive
def generate_alphabet_list():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters in the alphabet please.")
        generate_alphabet_list()
    else:
        print(output_list)

generate_alphabet_list()