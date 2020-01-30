from tkinter import *


class instruction_page(Frame):
   def __init__(self, master,call_on_selected):
       """Initialize Frame."""
       self.call_on_selected = call_on_selected
       super(instruction_page, self).__init__(master)
       self.grid()
       self.create_widgets()

   def create_widgets(self):
       self.story_txt = Text(self, width=100, height=15, wrap=WORD)
       self.story_txt.grid(row=0, column=0, columnspan=4)

       instructions = '''Are you ready to play one of the best games in the world?\n\nWith this version of Hangman, you get a chance to
play the classic game, while watching your hangman being drawn line by line!\n\nCan you save your hangman?\n\n\nFirst, select the single player button. \n\nThen, choose from one of the four categories to get words of that type.\n\nFinally, click the letter buttons to spell out the word, and win before it's too late!'''

       self.story_txt.delete(0.0, END)
       self.story_txt.insert(0.0, instructions)

       self.home_bttn = Button(self, text="home page", command=self.back_to_home
                          )
       Button(self, text="home page",
              command=self.back_to_home
              ).grid(row=5, column=0, sticky=W)

   def back_to_home(self):
       pass


