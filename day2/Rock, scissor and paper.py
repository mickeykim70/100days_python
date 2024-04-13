# Rock, scissor and paper
ROCK = 0
PAPER = 1
SCISSORS = 2

import random

while True:
    player = input("Let's play the game.. r(to ROCK), p(to PAPER), s(to SCISSORS) or Q(to quit) ? ")
    computer = random.randint(0,2)
    print(f"{computer= }")
    if player == 'q':
        break
    elif player == 'r':
        player = 0
    elif player == 'p':
        player = 1
    elif player == 's':
        player = 2
    print(f"{computer= }, {player= }")
    
    if computer == player:
        print(f"{computer=} vs {player=}. Draw")
    elif computer > player:
        if computer == SCISSORS:
            print(f"{computer=} vs {player=}. Player win")
        else:
            print(f"{computer=} vs {player=}. Computer win")
    else:
        print(f"{computer=} vs {player=}. Player win")
    
         
        
        
    


