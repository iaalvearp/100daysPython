#Step 2

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f"Pssst, the solution is {chosen_word}.")

#TODO-1: Create an empty List called display.
# For each leter in the chosen_word, add a "_" to 'display'.
# So if the chose_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()

display = []
for letter in chosen_word:
    display += "_" 

print(display)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# Angela's Solution
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

''' My solution #1
i = 0
for letter in chosen_word:
    if letter == guess:
        display[i] = letter
    i += 1
                #2
for position in range(len(chosen_word)):
    if guess == chosen_word[position]:
        display[position] = guess
    '''

#TODO-3: - Print 'display' and should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)