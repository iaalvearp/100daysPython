def greet_with(name, location):
    print(f"Hi {name}, how was your vacations in {location}?")

greet_with("Pedro Pascal", "Mexico")

def greet_default(name = "Juan", location = "It's not your bussines"):
    print(f"Hi {name}")
    print(f"Do you went to {location}")


greet_default("Wade")