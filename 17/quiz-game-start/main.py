from data import question_data as data
from api_data import api_data
from question_model import Question
from quiz_brain import QuizBrain


def create_questions(qs):
    list_of_questions = []
    for q in qs:
        item = Question(q["text"], q["answer"])
        list_of_questions.append(item)
    return list_of_questions


question_bank = create_questions(data)
print(len(question_bank))
api_question_bank = create_questions(api_data)
my_quiz = QuizBrain(question_bank)
my_second_quiz = QuizBrain(api_question_bank)

while my_quiz.still_has_questions():
    my_quiz.next_question()

print(f"Your final score: {my_quiz.score}/{len(my_quiz.question_list)}")

while my_second_quiz.still_has_questions():
    my_second_quiz.next_question()

print(
    f"Your final score: {my_second_quiz.score}/{len(my_second_quiz.question_list)}")
