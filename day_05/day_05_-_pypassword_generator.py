import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['#', '!', '$', '%', '&', '(', ')', '*', '+']

# Angela's solution
password_list = []
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Here is your password: {password}")


''' My solution
password = []
random_password = ''

print("Welcome to the PyPassword Generator!\n")

password_len = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

for number in range(0, numbers):
    password += numbers_list[random.randint(0, len(numbers_list) - 1)]
for letter in range(0, password_len):
    password += letters_list[random.randint(0, len(letters_list) - 1)]
for symbol in range(0, symbols):
    password += symbols_list[random.randint(0, len(symbols_list) - 1)]

for char in range(0, len(password)):
    pop_char = password.pop(random.randint(0, len(password)-1))
    random_password += pop_char

print(f"Here is your password: {random_password}")'''