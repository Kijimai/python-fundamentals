from tkinter import *
from turtle import update
from quiz_brain import QuizBrain

BG_COLOR = "#5ac8d8"
CANVAS_COLOR = "#2552ac"
COLOR_WHITE = "#FFFFFF"
QUIZ_FONT = ("Arial", 18, "italic")
LABEL_FONT = ("Arial", 16, "bold")
FLASH_CORRECT = "#70C441"
FLASH_WRONG = "#DA371B"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.current_score = self.quiz.score

        self.window = Tk()
        self.window.title("Quizmania")
        self.window.config(bg=BG_COLOR, padx=20, pady=20)

        self.canvas = Canvas(self.window, bg=CANVAS_COLOR,
                             width=300, height=250, highlightthickness=0)
        self.current_question = self.canvas.create_text(
            150, 125, font=QUIZ_FONT, width=280)
        self.canvas.itemconfig(
            self.current_question, text="Test text", fill=COLOR_WHITE)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=(50, 50))

        self.score_label = Label(
            text=f"Score: {self.current_score}", bg=BG_COLOR, fg=COLOR_WHITE, font=LABEL_FONT)
        self.score_label.grid(column=1, row=0)

        self.check_img = PhotoImage(file='./images/true.png')
        self.wrong_img = PhotoImage(file='./images/false.png')
        self.check_btn = Button(image=self.check_img, command=self.true_answer)
        self.x_btn = Button(image=self.wrong_img, command=self.false_answer)
        self.check_btn.grid(column=0, row=2)
        self.x_btn.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=CANVAS_COLOR)
        if self.quiz.still_has_questions:
            question_txt = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.current_question, text=question_txt)
        else:
            self.canvas.itemconfig(text="You have reached the end of the quiz!")
            self.check_btn.config(state="disabled")
            self.x_btn.config(state="disabled")
                    
    def true_answer(self):
        is_correct = self.quiz.check_answer("True")
        self.show_feedback(is_correct)

    def false_answer(self):
        is_correct = self.quiz.check_answer("False")
        self.show_feedback(is_correct)

    def update_score(self):
        self.current_score = self.quiz.score
        self.score_label.config(
            text=f"{self.current_score} / {self.quiz.question_number}")

    def show_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=FLASH_CORRECT)
        else:
            self.canvas.config(bg=FLASH_WRONG)
        self.window.after(1000, self.get_next_question)
