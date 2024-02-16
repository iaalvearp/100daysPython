#Step 3

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f"Pssst, the solution is {chosen_word}.")

#Create blanks
display = []
for letter in chosen_word:
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

finish_loop = False

#Angela's solution
# end_of_game = False
# while not end_of_game:

while finish_loop == False:
    guess = input("Guess a letter: ").lower()
    aux_word = ""

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        aux_word += display[position]

    print(display)

    '''Angela's solution
    if "_" not in display: # in operator heps to look into the lists and strings
        end_of_game = True
        print("You Win!!!")'''

    if aux_word == chosen_word:
        finish_loop = True
        print("You Win!!!")