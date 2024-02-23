from data import question_data
from random import choice
from question_model import Question
from quiz_brain import QuizBrain
# A class will be named using Pascal case without underscore "_"
# class User:
#     def __init__(self, user_id, user_name):
#         self.user_id = user_id
#         self.user_name = user_name
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User(123, "AlPes")
# user_2 = User(124, "Ali")
#
# user_1.follow(user_2)
#
# print(f"""
# {user_1.user_name}: following = {user_1.following} | followers = {user_1.followers}
# {user_2.user_name}: following = {user_2.following} | followers = {user_2.followers}
# """)

question_bank = []


# Angela's for loop
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# My for loop after see Angela's way
# for q in question_data:
#     question_bank.append(Question(q["text"], q["answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.new_question()

# Angela's solution
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# My solution
# quiz.finish_game()
