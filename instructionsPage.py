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

       instructions = ("Are you ready to play one of the best games in the world?\n\n"
                       "With this version of Hangman, you get a chance to play the classic game, while watching\nyour hangman being drawn line by line!\n\n"
                       "Can you save your hangman?\n\nFirst, select the play button.\n\nThen, choose from one of the categories to get words of that type. Random gives you"
                       " all of the catagories, and more.\n\n" 
                       "Finally, click the letter buttons to spell out the word, and win before it's too late!\n"
                       "Keep in mind that you only have 10 tries to get it right.\n\nAlso, even after the mouth of the hangman is drawn, you still have one more chance.\n\n"
                       "Good Luck and Have Fun!!!"
                       )

       self.story_txt.delete(0.0, END)
       self.story_txt.insert(0.0, instructions)

       self.home_bttn = Button(self, text="home page", command=self.back_to_home)

       Button(self, text="Home Page",
              font="Courier 20",
              fg="Dark Turquoise",
              command=self.back_to_home
              ).grid(row=5, column=0, sticky=W)

   def back_to_home(self):
       self.return_home()
