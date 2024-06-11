def get_numbers(file):

    with open(file, "r") as f:
        file_string = f.readlines()
        num_file = [int(string) for string in file_string]
        return num_file

file_1 = get_numbers("file1.txt")
file_2 = get_numbers("file2.txt")

result = [num for num in file_1 if num in file_2]
print(f"{result}")

file_1_set = set(file_1)
file_2_set = set(file_2)

print(f"{file_1_set.intersection(file_2_set)}")


