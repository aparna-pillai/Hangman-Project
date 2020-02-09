from tkinter import *


class Lose_screen(Frame):
   def __init__(self, master, choice):
       """Initialize Frame."""
       self.choice = choice
       super(Lose_screen, self).__init__(master)
       master.title("What a Loser!")
       self.grid()
       self.create_widgets()


   def create_widgets(self):
       print("LOSER!")