from tkinter import *


class Lose_screen(Frame):
   def __init__(self, master, choice, play_again):
       """Initialize Frame."""
       self.choice = choice
       self.play_again = play_again
       super(Lose_screen, self).__init__(master, background = "DodgerBlue4")
       master.title("What a Loser!")
       self.grid()
       self.create_widgets()


   def create_widgets(self):
       Label(self, text="Congratulations.",font="Courier 20 bold", fg="Dark Turquoise", bg = "DodgerBlue4"
             ).grid(row=0, column = 0, sticky=N)
       Label(self, text="You have lost.", font="Courier 20 bold", fg="Dark Turquoise", bg = "DodgerBlue4"
             ).grid(row=1, column=0, sticky=N)
       Label(self, text="", font="Courier 20 bold", fg="Dark Turquoise", bg = "DodgerBlue4"
             ).grid(row=2, column=0, sticky=N)
       Label(self, text="Your word was:", font="Courier 20 bold", fg="Dark Turquoise", bg = "DodgerBlue4"
             ).grid(row=3, column=0, sticky=N)
       Label(self, text=self.choice, font="Courier 20 bold", fg="Magenta", bg = "DodgerBlue4"
             ).grid(row=4, column=0, sticky=N)
       Label(self, text="", font="Courier 20 bold", fg="Dark Turquoise", bg="DodgerBlue4"
             ).grid(row=2, column=0, sticky=N)
       Button(self, text="Play Again!",
              font="Courier 12",
              fg="DodgerBlue4",
              bg="Dark Turquoise",
              command=self.back_to_home
              ).grid(row=5, column=0, sticky=W)

   def back_to_home(self):
       self.play_again()


