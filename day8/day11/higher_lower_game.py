### higher_lower_game

import random
from art import logo
from game_data import data

# 1. print welcome logo
print(logo)

# choose random question
def get_random_quesion():
    question = random.choice(data)
    return question

# filtering same question
def is_same_question(first, second):
    """Filtering same name?"""
    if first['name'] == second['name']:
        return True
    else:
        return False

# asking question
def asking_question(question_a, question_b):
    print(f"\nA: {question_a['name']} who is a {question_a['description']}, of {question_a['country']}.")
    print("vs")
    print(f"B: {question_b['name']} who is a {question_b['description']}, of {question_b['country']}. \n")
    
    
# 3. Judgement
def judgement(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == 'a'
    else:
        return guess == 'b'


# 5. main
def game():
    score = 0
    game_should_continue = True
    # generating questions
    question_a = get_random_quesion()
    question_b = get_random_quesion()   
    
    while game_should_continue:
        question_a = question_b
        question_b = get_random_quesion()
        
        is_same_question(question_a, question_b)
        asking_question(question_a, question_b)

        guess = input("Who has more followers? type 'a' or 'b' ").lower()
        follower_a = question_a['follower_count']
        follower_b = question_b['follower_count']
        
        print('\n')
        print(f"{question_a['name']} {follower_a= }")
        print(f"{question_b['name']} {follower_b= }")
        
        is_correct = judgement(guess, follower_a, follower_b)
        if is_correct:
            score += 1
            print(f"\nYou're right. current {score = }")
        else:
            print(f"\nSorry.  Final {score = } \n")
            game_should_continue = False
                
        
game()

