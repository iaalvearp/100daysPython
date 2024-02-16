import random


def guess_the_number():
    """Start the guess a number game"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    desition = input("Choose a difficulty. Type 'easy' or 'hard': ")
    chances = 0
    random_number = random.randint(0,100)

    if desition == "easy":
        chances = 10
    elif desition == "hard":
        chances = 5

    attempts = chances

    for _ in range(chances):
        print(f"You have {attempts} remaining to guess the number")
        attempts -= 1
        result = ""
        user_guess = int(input("Make a guess: "))
        if user_guess == random_number:
            return f"You got it! The answer was {random_number}."
        elif user_guess > random_number:
            result = "Too high.\nGuess again."
            print(result)
        elif user_guess < random_number:
            result = "Too low.\nGuess again."
            print(result)
        else:
            result = "Invalid input.\nGuess again."
            print(result)

    return f"You've run out of guesses, you lose. Right number was {random_number}"

game_result = guess_the_number()
print(game_result)