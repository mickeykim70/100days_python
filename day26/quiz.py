numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

squared_numbers = [number * number for number in numbers]

print(squared_numbers)


another_numbers = [9, 0, 32, 8, 2, 8, 64, 29, 42, 99]

even_numbers = [number for number in another_numbers if number % 2 == 0]

print(even_numbers)
