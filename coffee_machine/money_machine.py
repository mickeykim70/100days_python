# Money Machine
#       1) Check Money sufficient and accumulate money

class MoneyMachine:

    def __init__(self):
        self.COIN_VALUES = {
            "QUARTER": 0.25,
            "DIME": 0.1,
            "NICKLE": 0.05,
            "PENNY": 0.01,
        }
        self.profit = 0
        self.money_received = 0

    def is_money_ok(self, money, cost):
        if money >= cost:
            print(f"Here you go, exchange: ${money-cost}")
        else:
            print(f"Insert more money ${cost-money}")

    # def insert_coins(self):
    #     print(f"Input coins..")
    #     quarters = int(input("How many quarters? "))
    #     dimes = int(input("How many dimes? "))
    #     nickles = int(input("How many nickles? "))
    #     pennies = int(input("How many pennies? "))
    #
    #     total_coins = (quarters * self.COIN_VALUES["QUARTER"] +
    #                    dimes * self.COIN_VALUES["DIME"] +
    #                    nickles * self.COIN_VALUES["NICKLE"] +
    #                    pennies * self.COIN_VALUES["PENNY"])
    #
    #     return total_coins

    def insert_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received


    def do_report(self):
        """Prints the current profit"""
        print(f"Money: ${self.profit}")


    # def make_payment(self, cost):
    #     """Returns True when payment is accepted, or False if insufficient."""
    #     self.insert_coins()
    #     if self.money_received >= cost:
    #         change = round(self.money_received - cost, 2)
    #         print(f"Here is ${change} in change.")
    #         self.profit += cost
    #         self.money_received = 0
    #         return True
    #     else:
    #         print("Sorry that's not enough money. Money refunded.")
    #         self.money_received = 0
    #         return False