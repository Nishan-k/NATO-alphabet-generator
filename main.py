import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

user_input = list(input("Enter a word: "))
user_input = [letter.upper() for letter in user_input]

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
nato_word = [nato_dict[letter] for letter in user_input]
