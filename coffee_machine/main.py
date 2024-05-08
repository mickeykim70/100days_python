# Main: 1) Handling order
#       2) Handling coffee machine
#       3) Handling Money Machine

from coffee_machine import CoffeeMachine
from money_machine import MoneyMachine
from menu import Menu


coffee_machine = CoffeeMachine()
money_machine = MoneyMachine()
menu = Menu()

coffee_machine_is_on_now = True
while coffee_machine_is_on_now:
    menu_list = menu.get_items()
    my_order = input(f"What would you like to order? ({menu_list}): ")

    if my_order == "report":
        # call coffee machine to make report
        coffee_machine.do_report()
        money_machine.do_report()

    elif my_order == "off":
        # coffee machine off
        coffee_machine_is_on_now = False

    else:
        # 1) calling money_machine
        inserted_money = money_machine.insert_coins()
        beverage_costs = coffee_machine.menu[my_order]['cost']

        money_machine.is_money_ok(inserted_money, beverage_costs)

        # 2) calling coffee_machine
        coffee_machine.make_coffee(my_order)
