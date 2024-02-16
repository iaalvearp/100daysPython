# Addition
def add(num_1, num_2):
    return num_1 + num_2

# Substract
def substract(num_1, num_2):
    return num_1 - num_2

# Multiply
def multiply(num_1, num_2):
    return num_1 * num_2

# Divide
def divide(num_1, num_2):
    return num_1 / num_2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

# Angela's solution to the Calculator challenge
def calculator():
    num1 = float(input("What is your first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"The result of: {num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start again: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
print("Bye! ")
''' My solution Step 1
n1 = int(input("What is your first number? "))
select_operation = input("What operation you'll going to choose?\n+: Add\n-: Substract\n*: Multiply\n/: Divide\n")
n2 = int(input("What is your second number? "))
for symbol in operations:
    if select_operation == symbol:
        operation_function = operations[symbol]


print(f"The result of: {n1} {select_operation} {n2} = {operation_function(n1, n2)}")'''

''' My solution to the Calculator challenge
n1 = int(input("What is your first number? "))
for symbol in operations:
    print(symbol)
select_operation = input("What operation you'll going to choose? ")
n2 = int(input("What is your second number? "))
operation_function = operations[select_operation]
answer = operation_function(n1, n2)
print(f"The result of: {n1} {select_operation} {n2} = {answer}")
finish_loop = input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit: ")
loop_answer = answer

while finish_loop == "y":
    select_operation = input("What operation you'll going to choose? ")
    n3 = int(input("What is the next number? "))
    operation_function = operations[select_operation]
    acc_answer = operation_function(loop_answer, n3)
    print(f"The result of: {loop_answer} {select_operation} {n3} = {acc_answer}")
    finish_loop = input(f"Type 'y' to continue calculating with {acc_answer}, or 'n' to exit: ")
    loop_answer = acc_answer
'''