PLACE_HOLDER = '[name]'

with open("./input/names/invited_names.txt", "r", encoding="utf-8") as names:
    names = names.readlines()

for name in names:
    invited_name = name.strip()

    with open("./input/letters/starting_letter.txt", "r", encoding="utf-8") as letters:
        letter = letters.read()
        modified_letter = letter.replace(PLACE_HOLDER, invited_name)
        with open(f"./output/ReadyToSend/{invited_name}.txt", "w", encoding="utf-8") as invited_letter:
            invited_letter.write(modified_letter)






