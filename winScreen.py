from tkinter import *


class Win_screen(Frame):
   def __init__(self, master, play_again, game_exit):
       """Initialize Frame."""
       self.play_again = play_again
       self.exit = game_exit
       super(Win_screen, self).__init__(master, background ="DodgerBlue4")
       master.title("What a Winner!")
       self.grid()
       self.create_widgets()


   def create_widgets(self):
       Label(self, text="Congratulations!",font="Courier 20 bold", fg="Dark Turquoise", bg = "DodgerBlue4"
             ).grid(row=0, column = 0, sticky=N)
       Label(self, text="You have beat the system.", font="Courier 20 bold", fg="Dark Turquoise", bg = "DodgerBlue4"
             ).grid(row=1, column=0, sticky=N)
       Label(self, text="", font="Courier 20 bold", fg="Dark Turquoise", bg="DodgerBlue4"
             ).grid(row=2, column=0, sticky=N)
       Button(self, text="Play Again!",
              font="Courier 12",
              fg="DodgerBlue4",
              bg = "Dark Turquoise",
              command=self.back_to_home
              ).grid(row=5, column=0, sticky=W)
       Button(self, text="Exit",
              font="Courier 12",
              fg="DodgerBlue4",
              bg = "Dark Turquoise",
              command=self.leave()
              ).grid(row=5, column=1, sticky=W)


   def back_to_home(self):
       self.play_again()

   def leave(self):
       self.exit()
