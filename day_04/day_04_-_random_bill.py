import random

friends = input("Give me everybody's names, separated by a (,) coma: \n")
friends_list_split = friends.split(", ")
# friends_list = ["Angela", "Ben", "Jenny", "Michael","Chloe"]
list_long = len(friends_list_split) - 1
i = random.randint(0, list_long)

# Angela's solution
num_items = len(friends_list_split)
random_choice = random.randint(0, num_items - 1 )
person_who_pay = friends_list_split[random_choice]

# Easy way to do the same
person_who_will_pay = random.choice(friends_list_split)

print(f"{friends_list_split[i]} is going to buy the meal today!") # My way
print(f"{person_who_will_pay} is going to buy the meal today!") # Function's way
print(f"{person_who_pay} is going to buy the meal today!") # Angela's way
