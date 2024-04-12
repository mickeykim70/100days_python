# pizza order

# DECLARE CONSTANT
SMALL_SIZE = 15   # small size pizza PRICE
MEDIUM_SIZE = 20
LARGE_SIZE = 25
EXTRA_CHEEZE = 1
PEPPERONI_SMALL = 2
PEPPERONI_ML = 3  # for mid/large size pepperoni

price = 0


pizza_size = input("Order your pizza size? S, M or L ") 

if pizza_size == 'S':
    price += SMALL_SIZE 
elif pizza_size == 'M':
    price += MEDIUM_SIZE
else:
    price += LARGE_SIZE
    
add_pepperoni = input("Do you want to add more pepperoni? y or n ")
if add_pepperoni == 'y':
    if pizza_size == 'S':
        price += PEPPERONI_SMALL
    else:
        price += PEPPERONI_ML

add_extra_cheese = input("Do you want to add more extra cheese? y or n ")
if add_extra_cheese == 'y':
    price += EXTRA_CHEEZE
    
print(f"Total your order is ${price}.")


