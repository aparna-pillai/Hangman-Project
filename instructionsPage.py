from tkinter import *


class Instruction_page(Frame):
   def __init__(self, master, return_home):
       """Initialize Frame."""
       self.return_home = return_home
       super(Instruction_page, self).__init__(master)
       master.title("Instructions Page")
       self.grid()
       self.create_widgets()


   def create_widgets(self):
       self.story_txt = Text(self, font= "Courier 20", fg="Dark Cyan", width=100, height=18, wrap=WORD)
       self.story_txt.grid(row=0, column=0, columnspan=4)

       instructions = '''Are you ready to play one of the best games in the world?\n\nWith this version of Hangman, you get a chance to
play the classic game, while watching your hangman being drawn line by line!\n\nCan you save your hangman?\n\n\nFirst, select the single player button. \n\nThen, choose from one of the four categories to get words of that type.\n\nIf you are playing with a
friend, you can also click the "choose your own word" button to have your friend choose a custom word for you!\nFinally, click the letter buttons to spell out the word, and win before it's too late! Keep in mind that you only have 10 tries to get it right.'''

       self.story_txt.delete(0.0, END)
       self.story_txt.insert(0.0, instructions)

       self.home_bttn = Button(self, text="home page", command=self.back_to_home
                          )
       Button(self, text="Home Page",
              font="Courier 15",
              fg="Dark Turquoise",
              command=self.back_to_home
              ).grid(row=5, column=0, sticky=W)

   def back_to_home(self):
       self.return_home()
