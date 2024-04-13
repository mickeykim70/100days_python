import random

names = []

while True:
    ate_name = input("Enter the person who ate the meal today? LAST name is 'Q' ")
    if ate_name == 'Q':
        break
    names.append(ate_name)


total_person = len(names)
selected_person = random.randint(1, total_person)

print(f"{names[selected_person]} is going to buy meal today.")




