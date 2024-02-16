print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").capitalize()
add_pepperoni = input("Do you want pepperoni? Y or N: ").capitalize()
extra_cheese = input("Do you want extra cheese? Y or N: ").capitalize()
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3

if extra_cheese == "Y":
    bill += 1
    print(f"Total bill is ${bill}.")
else:
    print(f"Total bill is ${bill}.")