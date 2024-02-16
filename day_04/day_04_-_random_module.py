# This function has to be imported to be used
import random

# This function give a integer number bettwen and including the first and the last number
random_int = random.randint(1,10)
print(random_int)

# This function give a float number bettwen 0 - 1, 0 and 1 not included
random_float = random.random()
print(random_float)

# In this example random going to give a number bettwen 0 and 5, 0 and 5 not included
random_float *= 5
print(random_float)