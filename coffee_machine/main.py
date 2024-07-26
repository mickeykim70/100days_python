MENU = {
    "에스프레소": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "라떼": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "카푸치노": {
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

#check the resources sufficient?
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("미안합니다. {item}이 부족합니다.")
            return False
    return True


def process_coins():
    print("동전을 넣으세요.")

    total = int(input("Quarters? ")) * 0.25
    total += int(input("Dimes? ")) * 0.1
    total += int(input("Nickles? ")) * 0.05
    total += int(input("Pennies? ")) * 0.01

    return total



while True:
    user_order = input("무엇을 드시겠습니까? (에스프레소 / 라떼 / 카푸치노) ")

    if user_order == 'off':
        break

    elif user_order == 'report':
        print(f'Water: {resources["water"]}')
        print(f'milk: {resources["milk"]}')
        print(f'coffee: {resources["coffee"]}')

    elif user_order == '에스프레소':
        print('에스프레소')

    elif user_order == '라떼':
        print('라떼')

    elif user_order == '카푸치노':
        print('카푸치노')


