# Coffee Machine
#       1) Check Inventory & Report
#       2) Make coffee
#           - control ingredient amounts


class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.menu = {
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

    def do_report(self):
        print(f"water: {self.resources['water']}ml ")
        print(f"milk: {self.resources['milk']}ml ")
        print(f"coffee: {self.resources['coffee']}g ")

    def make_coffee(self, order):
        if order in self.menu:
            # print(f"order: {order}")
            # print(f"MENU: {self.menu[order]['ingredients']['water']} is ready for drinking")

            # print(self.resources['water'])

            for ingredient in self.menu[order]['ingredients']:
                self.resources[ingredient] -= self.menu[order]["ingredients"][ingredient]

                if self.resources[ingredient] <= 0:
                    print(f"Sorry {ingredient} is not enough")

            print(f"Here you go, {order}")


