

print("Welcome to the secret auction program.")
binders = {}
continue_loop = True
winner_bid = 0
winner_name = ""

while continue_loop:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    def adding_binders(binder_name, bind_amount):
        binders[binder_name] = bind_amount

    adding_binders(name, bid)
    

    confirmation = input("Do you want add another Binder? Type 'yes' or 'no': ")
    if confirmation == "no":
        continue_loop = False

for name in binders:
    actual_amount = binders[name]
    if actual_amount > winner_bid:
        winner_bid = actual_amount
        winner_name = name
print(f"The winner is: {winner_name} with a bid of: ${winner_bid}")