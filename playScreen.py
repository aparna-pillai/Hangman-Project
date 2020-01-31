from tkinter import *

class Play_screen(Frame):

   def __init__(self, master, choice):
       """Initialize Frame."""
       self.choice = choice
       super(Play_screen, self).__init__(master)
       master.title("Play Screen!")
       self.grid()
       self.create_widgets()

   def create_widgets(self):
       Button(self, text="A", fg = "white",bg = "navy",
              command=self.a
              ).grid(row=20, column=0, sticky=N)
       Label(self, text="         "
             ).grid(row=20, column=1, sticky=N)

   def a(self):
       pass
