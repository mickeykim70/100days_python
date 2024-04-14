# Hangman

# 1. preparing WORDs & STAGE
word_list = ["ardvark", "baboon", "camel"]
lives = 6  # set the LIFE

# 2. WORD for UNDERLINE
import random
chosen_word = random.choice(word_list)

#### testing code
print(f'Pssst, the solution is {chosen_word}.')

## prepare _ _ _ _ _ for WORD(chosen word)
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display.append('_')    

# 3. asking players to GUESS
end_of_game = False
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

# 4. GUESS in WORD ???
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
        lives -= 1   # life -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"{chosen_word= }")

    # Join all the elements in the list and turn it into a STRING.
    print(f"{' '.join(display)}")

     
    # END_GAME check(PLAYER WIN): underline is still in WORD??
    if "_" not in display:
        end_of_game = True
        print("You win")


