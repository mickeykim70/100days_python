from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_machine_on = True


while is_machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    # for maintainer command: "off"  //  "report"
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredient = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredient and is_payment_successful:
            coffee_maker.make_coffee(drink)


