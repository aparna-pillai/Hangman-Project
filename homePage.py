from tkinter import *
class Home_page(Frame):

   def __init__(self, master, call_on_selected, call_on_other_selected):
       """Initialize Frame."""
       self.call_on_selected = call_on_selected
       self.call_on_other_selected = call_on_other_selected
       super(Home_page, self).__init__(master)
       self.grid()
       self.create_widgets()

   def create_widgets(self):
       """Create widgets to get story information and to display story."""
       # create instruction label
       Label(self, text=""
             ).grid(row=0, column=0, sticky=N)

       Label(self, text="Welcome to", font="Courier 40 bold",
             fg="Navy Blue").grid(row=0, column=1, sticky=N)

       Label(self, text=""
             ).grid(row=0, column=2, sticky=N)

       Label(self,
             text="Hangman!", font="Courier 40 bold",
             fg="Navy Blue").grid(row=1, column=1, sticky=N)

       Label(self, text=""
             ).grid(row=2, column=1, sticky=N)

       Button(self, text="single player",
              font="fixedsys 15", bd=5,
              bg="Turquoise", command=self.single_player
              ).grid(row=3, column=1, sticky=N)

       Label(self, text=""
             ).grid(row=4, column=1, sticky=N)

       Button(self, text="instructions",
              font="fixedsys 15", bd=5,
              bg="#%2x%2x%2x" % (128, 192, 200), command=self.instructions
              ).grid(row=5, column=1, sticky=N)

   def single_player(self):
       self.call_on_other_selected()

   def instructions(self):
       self.call_on_selected()