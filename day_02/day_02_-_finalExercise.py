print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 o 15? %"))
customers = int(input("How many people to split the bill? "))
total_bill = bill + (bill * (tip / 100))
amount_per_customer = total_bill / customers

print("Each person should pay: $" + str(amount_per_customer))