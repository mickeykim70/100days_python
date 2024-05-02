import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[char] for char in word]
    except KeyError:
        print("Sorry, only letters please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
