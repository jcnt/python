from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quizparam: QuizBrain):
        self.quiz = quizparam

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, text="example text", fill="black", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)

        yesimg = PhotoImage(file="images/true.png")
        self.yes = Button(image=yesimg, highlightthickness=0)
        self.yes.grid(row=2, column=0)

        noimg = PhotoImage(file="images/false.png")
        self.no = Button(image=noimg, highlightthickness=0)
        self.no.grid(row=2, column=1)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("ARIAL", 18, "normal"))
        self.score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self): 
#         canvastext = self.quiz.next_question()
        canvastext = "some text"
        self.canvas.itemconfig(self.question_text, text=canvastext)


