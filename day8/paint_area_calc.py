import math

COVERAGE = 5

def paint_calc(height, width):
    cans = (height * width) / COVERAGE
    round_up_cans = math.ceil(cans)
    print(cans)
    print(f"You will need {round_up_cans} cans.")

test_h = int(input("Height of wall "))
test_w = int(input("Width of wall "))
    
paint_calc(test_h, test_w)
    
