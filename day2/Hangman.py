# Hangman

# 1. preparing WORDs & STAGE
from hangman_words import word_list
from hangman_art import stages, logo
import random

LIVES = 6  # set the LIFE
END_OF_GAME = False

print(logo)

# 2. WORD for UNDERLINE

chosen_word = random.choice(word_list)

#### testing code
print(f'Pssst, the solution is {chosen_word}.')

## prepare _ _ _ _ _ for WORD(chosen word)
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display.append('_')    

# 3. asking players to GUESS

while not END_OF_GAME:
    guess = input("\nGuess a letter: ").lower()

# 4. GUESS in WORD ???
    # repeating tries warning
    if guess in display:
        print(f"You've already guessed {guess}")

    ## replace the letter in THE POSITION
    ##  a _ _ l _
    for position in range(word_length): # to assign ONE character to letter 
        letter = chosen_word[position]  
    
        if letter == guess:
        ## 4-1 ___yes___
            display[position] = letter  # replace underline with CORRECT

        ## 4-2 ___no___
        
    # END_GAME check(PLAYER LOOSE):    
    if guess not in chosen_word:
        LIVES -= 1   # life -= 1
        # Wrong guess!
        print(f"You guessed {guess}, that's not in the word. You lose a life. {LIVES} left.")
        
        if LIVES == 0:
            END_OF_GAME = True
            print("You lose.")
            print(f"{chosen_word= }")
            
        

    # Join all the elements in the list and turn it into a STRING.
    print(f"{' '.join(display)}")

     
    # END_GAME check(PLAYER WIN): underline is still in WORD??
    if "_" not in display:
        END_OF_GAME = True
        print("You win")

    # printing stages ascii
    print(stages[LIVES])
