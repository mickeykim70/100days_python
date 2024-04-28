PLACE_HOLDER = "[name]"


with open("./Mail Merge Project Start/input/names/invited_names.txt", "r") as invited_names:
    names = invited_names.read().splitlines()
    print(names)


with open("./Mail Merge Project Start/input/letters/starting_letter.txt", "r") as starting_letters:
    letter_contents = starting_letters.read()

    for name in names:
        new_letter = letter_contents.replace(PLACE_HOLDER, name)

        with open(f"./Mail Merge Project Start/output/Ready to send/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)



