#Step 4

import random
import hangman_art
import hangman_words


chosen_word = random.choice(hangman_words.animals)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

#Testing code
#print(f"Pssst, the solution is {chosen_word}.")

#Printing logo from module
print(hangman_art.logo)
#Angela's solution to import logo
# from hangman_art import logo, stages # with a coma (,) is possible import more than one thing from the module
# print(logo)

#Create blanks
display = []
for letter in chosen_word:
    display += "_"

end_of_game = False
lives = 6
print(f"{' '.join(display)}")

while not end_of_game:
    print(hangman_art.stages[lives])
    guess = input("Guess a letter: ").lower()
    inside = False

    #Check if the letter is already in
    if guess in display:
        print(f"You've already guessed: {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            inside = True # Angela's solution doesn't need this variable
    if not inside == True:
        lives -= 1
        print(f"Yoy guessed: {guess}, that's not in the word. You lose a life.")
    
    #Angela's solution to exit when user lose.
    #if guess not in chosen_word:
    #    lives -= 1
    #    if lives == 0:
    #        end_of_game = True
    #        print("You lose.")

#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
        
    if not lives > 0:
        end_of_game = True
        print(hangman_art.stages[0])
        print(f"You lose. The correct word was: {chosen_word}")

    

#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."


#Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    