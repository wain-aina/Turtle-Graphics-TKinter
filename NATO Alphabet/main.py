import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# In dataframes you must use index and row in the for loop
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def ask():
    word = input("Enter a word: ").upper()

    try:
        output = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        ask()
    else:
        print(output)

ask()