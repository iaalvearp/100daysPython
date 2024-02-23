from data import question_data

# My solution to the entire challenge
# class QuizBrain:
#     def __init__(self, lists):
#         self.question_number = 0
#         self.question_list = lists
#
#         def next_question():
#             score = 0
#             for q in lists:
#                 q_text = q.q_text
#                 q_answer = q.q_answer
#                 self.question_number += 1
#                 user_answer = input(f"Q{self.question_number}: {q_text} (True/False)?: ")
#                 if q_answer != user_answer:
#                     return print(f"You got it Wrong!\nThe correct answer was: {q_answer}.\n"
#                                  f"You current score is: {score}/{self.question_number}")
#                 else:
#                     score += 1
#                     print(f'''
#                     You got it right!
#                     The correct answer was: {q_answer}.
#                     You current score is: {score}/{self.question_number}
#                     ''')
#         next_question()


# Angela's solution
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        # Angela's solution
        return self.question_number < len(self.question_list)
        # if self.question_number > len(self.question_list): # My solution
        #     return False
        # else:
        #     return True

    def new_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.q_text} (True/False)?: ")
        self.check_answer(user_answer, current_question.q_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Yur current score is: {self.score}/{self.question_number}\n")

    def finish_game(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.score}/{self.question_number}")
        # My solution
        # current_answer = self.question_list[self.question_number]
        # if current_answer == self.user_answer:
        #     self.score += 1
    
