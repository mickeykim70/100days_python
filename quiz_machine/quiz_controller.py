class QuizController:

    def __init__(self, q_list):
        self.hit_score = 0
        self.current_quiz_number = 0
        self.quiz_list = q_list

    def still_has_quizzes(self):
        if self.current_quiz_number < len(self.quiz_list):
            return True
        else:
            return False

    def next_quiz(self):
        current_quiz = self.quiz_list[self.current_quiz_number]
        self.current_quiz_number += 1

        user_answer = input(f"Q.{self.current_quiz_number}: {current_quiz.text} ").lower()
        self.check_answer(user_answer, current_quiz.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct answer!!")
            self.hit_score += 1
        else:
            print("Wrong answer...")

        print(f"The correct answer is {correct_answer}")
        print(f"Your current score: {self.hit_score}/{len(self.quiz_list)} \n")

