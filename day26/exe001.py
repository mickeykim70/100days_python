with open ("file1.txt", "r") as f1:
    file_list1 = f1.read().splitlines()

with open ("file2.txt", "r") as f2:
    file_list2 = f2.read().splitlines()

result = [int(num) for num in file_list1 if num in file_list2]

print(result)

