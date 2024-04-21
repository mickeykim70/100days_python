from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_machine_on_now = True
while is_machine_on_now:
    choice = input(f"Please order here. {menu.get_items()} ")

    if choice == 'off':
        is_machine_on_now = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        ordered_drink = menu.find_drink(choice)
        is_enough_ingredient = coffee_maker.is_resource_sufficient(ordered_drink)
        is_payment_enough = money_machine.make_payment(ordered_drink.cost)
        if is_enough_ingredient and is_payment_enough:
            coffee_maker.make_coffee(ordered_drink)

