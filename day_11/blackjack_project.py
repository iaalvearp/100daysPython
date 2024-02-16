import random

cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ace_checker(input_list):
    """Replace 11 with an 1 when the sum is over 21"""
    if 11 in input_list and sum(input_list)  > 21:
        input_list.remove(11)
        input_list.append(1)

def blackjack():
    """Function to start the game"""
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_game == "n":
        say_bye = print("Bye")
        return say_bye
    user_cards = []
    pc_cards = []
    for _ in range(2):
        pop_card_user = random.choice(cards_list)
        card_index_user = cards_list.index(pop_card_user)
        user_cards.append(pop_card_user)
        cards_list.pop(card_index_user)
        pop_card_pc = random.choice(cards_list)
        card_index_pc = cards_list.index(pop_card_pc)
        pc_cards.append(pop_card_pc)
        cards_list.pop(card_index_pc)
    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {pc_cards[0]}")
    want_card = True
    while want_card:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            pop_card_user = random.choice(cards_list)
            card_index_user = cards_list.index(pop_card_user)
            user_cards.append(pop_card_user)
            cards_list.pop(card_index_user)
            ace_checker(user_cards)
            if sum(user_cards) > 21:
                print(f"Your cards: {user_cards} Total: {sum(user_cards)}.")
                print(f"Computer's cards: {pc_cards}")
                want_card = False
                print("You lose.")
                return blackjack()
            else:
                print(f"Computer's first card: {pc_cards[0]}")
                print(f"Your cards: {user_cards}")
        else:
            want_card = False
    while sum(pc_cards) < 17:
        pop_card_pc = random.choice(cards_list)
        card_index_pc = cards_list.index(pop_card_pc)
        pc_cards.append(pop_card_pc)
        cards_list.pop(card_index_pc)
        ace_checker(pc_cards)
    print(f"Your cards: {user_cards} Total: {sum(user_cards)}.")
    print(f"Computer's cards: {pc_cards} Total: {sum(pc_cards)}.")

    if sum(pc_cards) <= 21 and sum(pc_cards) > sum(user_cards):
        print("You lose")
    elif sum(pc_cards) > 21 and sum(user_cards) < 21:
        print("You Win")
    elif sum(pc_cards) < sum(user_cards):
        print("You Win")
    else:
        print("It's a draw.")

    blackjack()



blackjack()