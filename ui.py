from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window= Tk()
        self.window.title("quiz")
        self.window.config(padx=20,pady=20,bg= THEME_COLOR)
        self.score_label= Label(text= "Score: 0",fg= "white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas= Canvas(width=300, height=250, bg="white")
        self.question_text= self.canvas.create_text(150,125,text="some text", fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        right_image= PhotoImage(file="images/true.png")
        self.right_button= Button(image=right_image,highlightthickness=0,command=self.true_pressed)
        self.right_button.grid(row=2,column= 0)

        wrong_image= PhotoImage(file="images/false.png")
        self.wrong_button= Button(image=wrong_image,highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(row=2,column= 1)

        





        self.window.mainloop()
