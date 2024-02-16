import random

pc_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type:\n0: Rock\n1: Paper\n2: Scissors.\n"))
options = ["Rock", "Paper", "Scissors"]

# Angela's Solution
if user_choice >= 3 or user_choice < 0:
    print("Invalid choice. You lose.")
else:
    if user_choice == 2 and pc_choice == 0:
        print(f"User: {options[user_choice]}")
        print(f"Computer: {options[pc_choice]}")
        print("You lose.")
    elif user_choice == 0 and pc_choice == 2:
        print(f"User: {options[user_choice]}")
        print(f"Computer: {options[pc_choice]}")
        print("You Win.")
    elif user_choice > pc_choice:
        print(f"User: {options[user_choice]}")
        print(f"Computer: {options[pc_choice]}")
        print("You Win!!!")
    elif user_choice < pc_choice:
        print(f"User: {options[user_choice]}")
        print(f"Computer: {options[pc_choice]}")
        print("You lose.")
    elif user_choice == pc_choice:
        print(f"User: {options[user_choice]}")
        print(f"Computer: {options[pc_choice]}")
        print("It's a draw.")
    else:
        print("Invalid choice. You lose.")

''' My solution
if user_choice == 0 and pc_choice == 0:
    print(f"You: {options[user_choice]}.\nComputer: {options[pc_choice]}.\nTied! Try again!!")
elif user_choice == 0 and pc_choice == 1:
    print(f"You: {options[user_choice]}.\nComputer: {options[pc_choice]}.\nYou lose")
elif user_choice == 0 and pc_choice == 2:
    print(f"You: {options[user_choice]}.\nComputer: {options[pc_choice]}.\nYou Win!!!")

if user_choice == 1 and pc_choice == 1:
    print(f"You: {options[user_choice]}.\nComputer: {options[pc_choice]}.\nTied! Try again!!")
elif user_choice == 1 and pc_choice == 2:
    print(f"You: {options[user_choice]}.\nComputer: {options[pc_choice]}.\nYou lose")
elif user_choice == 1 and pc_choice == 0:
    print(f"You: {options[user_choice]}.\nComputer: {options[pc_choice]}.\nYou Win!!!")

if user_choice == 2 and pc_choice == 2:
    print(f"You: {options[user_choice]}.\nComputer: {options[pc_choice]}.\nTied! Try again!!")
elif user_choice == 2 and pc_choice == 0:
    print(f"You: {options[user_choice]}.\nComputer: {options[pc_choice]}.\nYou lose")
elif user_choice == 2 and pc_choice == 1:
    print(f"You: {options[user_choice]}.\nComputer: {options[pc_choice]}.\nYou Win!!!")'''