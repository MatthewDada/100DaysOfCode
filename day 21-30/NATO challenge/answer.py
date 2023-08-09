import pandas as pd
filepath = "day 21-30\\NATO challenge\\nato_phonetic_alphabet.csv"
data = pd.read_csv(filepath)

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# print(alphabet_dict)

word = input("Enter a word: ").upper()
output = [alphabet_dict[letter] for letter in word]
print(output)
