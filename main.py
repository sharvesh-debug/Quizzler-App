from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import UserInterface
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
User_inter=UserInterface(quiz)

