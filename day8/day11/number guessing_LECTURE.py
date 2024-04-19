### number guessing

# 1. generating random number
import random

# global constant
EASY_TURNS = 10
HARD_TURNS = 5


# 3. function -- check the NUMBERS each other
def check_answer(guess, answer, turns):
    """Returns the number of remaining and high/low"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}.")
# 4. function -- set difficulties
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_TURNS
    else:
        return HARD_TURNS

def game():
# Choosing random number 1 - 100
    print("Welcome to the Number Guessing Game!")
    print("Computer is thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)
    print(f"Pssst. the correct answer is {random_number}")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining.")

    guess = 0
    # repeat the guessing
    while guess != random_number:
        
        # Let the user guesses a number
        guess = int(input("Make a guess: "))
        check_answer(guess, random_number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

game()


