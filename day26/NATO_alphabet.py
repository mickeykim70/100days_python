import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data = pd.DataFrame(data)

code = {row.letter:row.code for (index, row) in data.iterrows()}

sentence = input("Enter a sentence: ").upper()

phonetic_character = [code[char] for char in sentence]
print(phonetic_character)