print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm? "))
bill = 0
photo_price = 3

if height >= 120:
    print("You can ride the rollercoaster!!!")
    user_age = int(input("How old are you? "))
    if user_age <= 12:
        bill = 5
        print(f"Child tickets are ${bill}.")
    elif user_age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}.")
    elif user_age >= 45 and user_age <= 55:
        print("Everything is going to be Ok. Have a free ride on us!.")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}.")
    
    photo = input("Do you want a photo? Y or N: ").capitalize()
    
    if photo == "Y":
        bill += photo_price

    print(f"Total bill will be ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride!")