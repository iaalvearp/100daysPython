
# # Problem #1 - Debug Odd or even number
# number = int(input("Wich number do you want to check?"))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# # Problem #2 - Debug Leap year checker
# year = int(input("Wich year do you want to check?"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not lear year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# Problem #3 Debug FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)