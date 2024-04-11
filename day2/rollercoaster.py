print("Welcome to the rollercoaster!!")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age > 18 :
        print("Pay for $11")
    elif age >= 12:
        print("Pay for $7")
    else:
        print("Pay for $5")
    
else:
    print("Sorry, you have to grow taller before you ride.")
