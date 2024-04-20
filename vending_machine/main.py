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

# global variable and CONSTANTS
is_on = True  # machine is working now
profit = 0
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def is_resources_sufficient(order_ingredients):
    """Return "True" when order can be made or "False" (insufficient)"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry. There is not enough {item}.")
            return False
        return True


# TODO 5. Process coins.
def process_coins():
    """Return total calculated money... when coins inserted."""
    print("Please insert coins.")
    total_calculated_money = int(input("How many quateres? ")) * quarters
    total_calculated_money += int(input("How many dimes? ")) * dimes
    total_calculated_money += int(input("How many nickles? ")) * nickles
    total_calculated_money += int(input("How many pennies? ")) * pennies
    return total_calculated_money


# TODO 6. Check transaction successful?
def is_transaction_successful(money_received, drink_cost):
    """Return 'True' when the money_received > drink_cost """
    if money_received >= drink_cost:
        changes = round(money_received - drink_cost, 2)
        print(f"Here is ${changes} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO 7. Make a coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == 'off':
        is_on = False
    # TODO 3. Print report.
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    # TODO 4. Check resources sufficient?
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



    # a. If the transaction is successful and there are enough resources to make the drink the
    # user selected, then the ingredients to make the drink should be deducted from the
    # coffee machine resources.
    # E.g. report before purchasing latte:
    # Water: 300ml
    # Milk: 200ml
    # Coffee: 100g
    # Money: $0
    # Report after purchasing latte:
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
    # b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
    # latte was their choice of drink.