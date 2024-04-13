# Finding Average Height

student_heights = []
while True:
    i = input("Student heights? , q to quit  ")
    if i == 'q':
        break
    student_heights.append(i)

sum_height = 0
for height in student_heights:
    sum_height += int(height)
print(sum_height)

number_student = 0
for _ in student_heights:
    number_student += 1
print(number_student)    
        
average_of_heights = round(sum_height / number_student)
print(average_of_heights)         
    



