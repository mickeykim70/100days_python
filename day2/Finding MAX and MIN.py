# Finding MAX and MIN

student_scores = []
while True:
    i = input("Student Scores? , q to quit  ")
    if i == 'q':
        break
    student_scores.append(i)

max_score = 0
for score in student_scores:
    if int(score) > int(max_score):
        max_score = score
        
print(f"{max_score=}")


    
    
    
    
    