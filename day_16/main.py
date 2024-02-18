from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
cash = MoneyMachine()
is_on = True

while is_on:
    user_choice = input(f"Select your coffee form our Menu: {menu.get_items()}\n")

    if user_choice == "report":
        machine.report()
        cash.report()
    elif menu.get_items().find(user_choice) >= 0:
        menu_item = menu.find_drink(user_choice)
        item_cost = menu.find_drink(user_choice).cost
        if machine.is_resource_sufficient(menu_item):
            if cash.make_payment(item_cost):
                machine.make_coffee(menu_item)
            else:
                print("Not enough money. Money refunded.")
    elif user_choice == "off":
        is_on = False
    else:
        print(f"'{user_choice}' isn't a valid choice.")
