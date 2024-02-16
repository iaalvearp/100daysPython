MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}


def print_report(obj):
    """Print the resources status"""
    print(f"Water: {obj['water']}ml")
    print(f"Milk: {obj['milk']}ml")
    print(f"Coffee: {obj['coffee']}g")
    print(f"Money: ${obj['money']}")


def money_counter(coin_list):
    print("Please insert coins.")
    total_money = 0
    for coin in coin_list:
        money = int(input(f"How many {coin}?: "))
        total_money += money * coin_list[coin]
    return total_money


def check_ingredients(choice, menu, initial_resources):
    result = True
    for ingredient in menu[choice]['ingredients']:
        if initial_resources[ingredient] >= menu[choice]['ingredients'][ingredient]:
            result *= 1
        else:
            return ingredient
    return result


def make_coffee(choice, menu, initial_resources):
    for ingredient in menu[choice]['ingredients']:
        initial_resources[ingredient] -= menu[choice]['ingredients'][ingredient]
    initial_resources['money'] += menu[choice]['cost']
    return initial_resources


resources['money'] = 0
is_on = True


while is_on:
    change = 0
    election = input("What would you like? (espresso/latte/cappuccino): ")
    if election == "off":
        is_on = False
    elif election == "report":
        print_report(resources)
    elif election == "espresso" or election == "latte" or election == "cappuccino":
        if check_ingredients(election, MENU, resources) == 1:
            payment = money_counter(coins)
            if payment < MENU[election]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = payment - MENU[election]['cost']
                make_coffee(election, MENU, resources)
                print(f"Here's ${round(change, 2)} in change.")
                print(f"Here's your ☕ {election}!")
        else:
            print(f"Sorry there's not enough {check_ingredients(election, MENU, resources)}")
    else:
        print(f"{election} it's not a valid input")
