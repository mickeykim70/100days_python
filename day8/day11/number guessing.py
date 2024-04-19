### number guessing

# 1. generating random number
import random

random_number = random.randint(1, 100)

# 2. choose difficulties
print("Welcome to the Number Guessing Game!")
print("Computer is thinking of a number between 1 and 100.")

difficulties = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulties == 'easy':
    attempt = 10
else:
    attempt = 5

# 3. function -- guessing numbers 


def guessing_numbers(guessing):
    if random_number == guessing:
        return 'matched'
    elif random_number > guessing:
        return 'low'
    else:
        return 'high'


# call function as difficulties
while attempt:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guessing = int(input("Make a guess: "))
    
    result = guessing_numbers(guessing)
    
    if result == 'matched':
        print(f"Succeed")
        break
    elif result == 'high':
        print(f"too high... guess again: ")
        attempt -= 1
    else:
        print(f"too low... guess again: ")
        attempt -= 1
        
print(f" {random_number=}")
    





    

# 4. finalizing

