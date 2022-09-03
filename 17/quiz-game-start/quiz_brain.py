class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, answer, current_question_answer):
        if answer.lower() == current_question_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        print(f"The correct answer was: {current_question_answer}.")

    def next_question(self):
        current_question_number = self.question_number + 1
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        correct_answer = current_question.answer
        user_answer = input(
            f"Question number {current_question_number}: {current_question.text} (True/False)\n")
        self.check_answer(
            user_answer, correct_answer)
        print(f"Your current score is: {self.score}/{current_question_number}")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
