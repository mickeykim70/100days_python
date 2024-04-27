##### Resouces

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
    "capuccino": {
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


# Declare Global variables and Constants

is_machine_on = True
profit = 0


def is_resources_sufficient(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry. {ingredient} is not enough.")
            return False
    return True


def adding_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    return total


def is_money_correct(received_money, chosen_menu_cost):
    if received_money >= chosen_menu_cost:
        changes = round(received_money - chosen_menu_cost, 2)
        print(f"Here is ${changes} in change.")
        global profit
        profit += chosen_menu_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(beverage_name, beverage_ingredients):
    for ingredient in beverage_ingredients:
        resources[ingredient] -= beverage_ingredients[ingredient]

    print(f"Enjoy your {beverage_name}.")


# MAIN loop
while is_machine_on:
    choice = input("What would you like? (espresso/latte/capuccino): ")

    # for Maintainer use only. 'report' / 'off'
    if choice == 'off':   # machine off
        is_machine_on = False
    elif choice == 'report':
        print(f"{resources['water']}ml")
        print(f"{resources['milk']}ml")
        print(f"{resources['coffee']}g")
        print(f"{profit}")
    else:
        chosen_menu = MENU[choice]
        # check resources (sufficient) every order
        if is_resources_sufficient(chosen_menu['ingredients']):
            # check inserted money is sufficient
            inserted_coins = adding_coins()
            if is_money_correct(inserted_coins, chosen_menu['cost']):
                make_coffee(choice, chosen_menu['ingredients'])



