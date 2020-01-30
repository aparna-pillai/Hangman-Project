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
       pass
