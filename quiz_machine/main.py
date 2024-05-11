import html
from data import question_data
from question_model import Question
from quiz_controller import QuizController

question_list = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"].lower()
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)

quiz_controller = QuizController(question_list)
quiz_controller.next_quiz()

while quiz_controller.still_has_quizzes:
    print(type(quiz_controller.still_has_quizzes))
    quiz_controller.next_quiz()
    print(quiz_controller.still_has_quizzes)

