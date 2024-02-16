from random import randint
from art import logo
from art import vs
from game_data import data

print(logo)
def select_character(char):
    return f"{char['name']}, a {char['description']}, from {char['country']}."

def followers_ammount(char):
    return char['follower_count']

def compare_character():
    character_a = data[randint(0, len(data) - 1)]
    is_winning = True
    score = 0

    while is_winning:
        character_b = data[randint(0, len(data) - 1)]
        followers_a = followers_ammount(character_a)
        followers_b = followers_ammount(character_b)

        if followers_a == followers_b:
            character_b = data[randint(0, len(data) - 1)]
            followers_b = followers_ammount(character_b)

        print(f"Compare A: {select_character(character_a)}")

        print(vs)

        print(f"Against B: {select_character(character_b)}")

        desition = input("Who has more followers? Type 'A' or 'B': ").lower()

        if desition == "a":
            if followers_a > followers_b:
                character_a = character_a
                followers_a = followers_a
            else:
                return f"Sorry, that's wrong. Final score: {score}"
        else:
            if followers_a < followers_b:
                character_a = character_b
                followers_a = followers_b
            else:
                return f"Sorry, that's wrong. Final score: {score}"

        score += 1

print(compare_character())