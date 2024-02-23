from data import question_data
from random import choice


text_to_show = choice(question_data)


# My solution. Only work with this example but not with others. I get it now.
class QuizMaker:
    def __init__(self, selected_text):
        self.text = selected_text["text"]
        self.answer = selected_text["answer"]


# Angela's solution
class Question:
    def __init__(self, q_text, q_answer):
        self.q_text = q_text
        self.q_answer = q_answer
