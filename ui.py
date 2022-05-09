from cProfile import label
from cgitb import text
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
class QuizUi:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("quizzler")
      
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=300,height=250,bg='white')

        self.question_text=self.canvas.create_text(150,125,width=280,text="helooo",font=("Ariel",20,"italic"),fill=THEME_COLOR)
        #here canvas.create text needs to take position x,y as parameter otherwise error will show.
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)


        self.scorelabel=Label(text="score :0",fg="white",bg=THEME_COLOR)
        self.scorelabel.grid(row=0,column=1)
        trueimage=PhotoImage(file="images/true.png")
        self.truebutton=Button(image=trueimage,highlightthickness=0,command=self.check_true)
        self.truebutton.grid(row=2,column=0)
        falseimage=PhotoImage(file="images/false.png")
        self.falsebutton=Button(image=falseimage,highlightthickness=0,command=self.check_false)
        self.falsebutton.grid(row=2,column=1)
        self.get_next_ques()
        self.window.mainloop()
       
    def get_next_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
          self.scorelabel.config(text=f"{self.quiz.score}")
       
          q_text= self.quiz.next_question()
          self.canvas.itemconfig(self.question_text,text=q_text)
        else:
         self.canvas.itemconfig(self.question_text,text="you have reached  end!")
         self.truebutton.config(state="disabled")
         self.falsebutton.config(state="disabled")

   
    def check_true(self):
       
     self.give_feedback(self.quiz.check_answer("True"))
        
    def check_false(self):
       
      self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_ques)






  

