print("Welcome to Tresure Island.\nYour mission is to find a the treasure.\nYou're at a cross road. Where do you want to go? Type \"left\" or \"right\"")
first_choice = input().lower()
if first_choice == "left":
    print("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" across.")
    second_choice = input().lower()
    if second_choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. On red, one yellow and one blue. Wich colour do you choose?")
        third_choice = input().lower()
        if third_choice == "yellow":
            print("You found the treasure. You win!!!")
        elif third_choice == "red":
            print("It's a room full of fire. Game Over.")
        elif third_choice == "blue":
            print("Eaten by beasts. Game Over.!!!")
        else:
            print("You chose a door that doesn't exist. Game Over!!!")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over!!!")
