# Prime number
import math
def prime_checker(number):
    is_prime = True
    root_num = int(math.sqrt(number))
    for i in range(2, root_num):
        if root_num % i == 0:
            is_prime = False
            
    if is_prime:
        print(f"{number} is a prime number.")
        
    else:
        print(f"{number} is NOT prime number.")
            
curious_number = int(input("Input your curious number... "))

prime_checker(curious_number)

