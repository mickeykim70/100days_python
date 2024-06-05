from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


#question_bank["question_text","question_answer"]
#Question[question_text, question_answer]

# for index in range(len(question_data)):
#     question_bank.append(question_data[index]["question"])
#     print(question_bank[index])
    
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer) 
    question_bank.append(new_question)
    
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Completed!!")
print(f"Your final score: {quiz.score} / {quiz.question_number}")
    
