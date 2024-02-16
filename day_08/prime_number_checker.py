''' 
def prime_checker(number):
    if number == 2 or number == 3 or number == 5 or number == 7:
        print(f"{number} is a prime number")
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")'''

# Angela's solution     
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    
    if is_prime:
        print(f"It's a prime number.")
    else:
        print(f"It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)