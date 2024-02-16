import random
# Step 1

word_list = ["ardvark", "baboon", "camel"]

#TODO-1- Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# My solution
# chosen_word = word_list[random.randint(0, len(word_list) - 1)]

# Angela's solution
chosen_word = random.choice(word_list)

#TODO-2- Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

#TODO-3- Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# Angela's solution
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

''' My solution
for i in range(0, len(chosen_word)):
    if chosen_word[i] == guess:
        print("True")
    else:
        print("False")'''