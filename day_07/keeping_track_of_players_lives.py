#Step 4

import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

#Testing code
print(f"Pssst, the solution is {chosen_word}.")

#Create blanks
display = []
for letter in chosen_word:
    display += "_"

end_of_game = False
lives = 6
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    inside = False
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            inside = True
    if not inside == True:
        lives -= 1
#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."

#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

#Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    if not lives > 0:
        end_of_game = True
        print("You lose.")