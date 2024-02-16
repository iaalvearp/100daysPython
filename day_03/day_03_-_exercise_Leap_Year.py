print("Welcome to the Leap Year Verificator")
user_year = int(input("Write a year: "))

if user_year % 4 == 0:
    if user_year % 100 == 0 and user_year % 400 != 0:
        print(f"{user_year} is NOT a Leap Year!")
    else:
        print(f"{user_year} is a Leap Year!")
else:
    print(f"{user_year} is NOT a Leap Year!")