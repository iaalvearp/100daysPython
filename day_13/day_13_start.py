from random import randint
############DEBUGGING#####################

# Describe Problem
def my_function():
    """Return a message once it reaches number 20"""
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()

# Reproduce the Bug
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

# Fix the Errors
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")

#Print is Your Friend
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"Total words are: {total_words}")

#Use a Debugger
def mutate(a_list):
    """Return a new list with the input list's value multiply by 2"""
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])