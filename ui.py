from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class UserInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.window=Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.score_display=Label(text=f"score:{quiz_brain.score}",fg="white",bg=THEME_COLOR)
        self.score_display.grid(row=0, column=1)
        self.canvas=Canvas(bg="white",height=250,width=300)
        self.t="something to display"
        self.question=self.canvas.create_text(150,125,text=f"{self.t}",font=("Arial",20,"italic"),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2)
        self.right_image=PhotoImage(file="./images/true.png")
        def answer_may_true():
            feed_backer(quiz_brain.check_answer("True"))
        def answer_may_false():
            feed_backer(quiz_brain.check_answer("False"))
        self.right_button=Button(image=self.right_image,highlightthickness=0,command=answer_may_true)
        self.right_button.grid(row=2,column=0)
        self.wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0,command=answer_may_false)
        self.wrong_button.grid(row=2, column=1)
        def next_question_generator():
            self.canvas.config(bg="white")
            if quiz_brain.still_has_questions():
                t = quiz_brain.next_question()
                self.score_display.config(text=f"Score:{quiz_brain.score}/10")
                self.canvas.itemconfig(self.question, text=t)
            else:

                self.canvas.itemconfig(self.question, text="you have reached the end")
                self.right_button.config(state="disabled")
                self.wrong_button.config(state="disabled")





        next_question_generator()
        def feed_backer(is_right:bool):
            if is_right:
                self.canvas.config(bg="green")
                self.window.after(1000,next_question_generator)

            else:
                self.canvas.config(bg="red")
                self.window.after(1000, next_question_generator)





        self.window.mainloop()







