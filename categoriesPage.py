from tkinter import *

import random
class Categories_page(Frame):
   def __init__(self, master,call_on_next):
       """Initialize Frame."""
       self.call_on_next = call_on_next
       super(Categories_page, self).__init__(master)
       self.grid()
       self.create_widgets()
       master.title("Categories")

   def create_widgets(self):
       Label(self, text="",
             ).grid(row=0, column=0, sticky=N)
       Label(self, text="",
             ).grid(row=0, column=2, sticky=N)
       Button(self, text="Food", font = "Courier 20", fg="Dodger Blue",
              command=self.food_choice
              ).grid(row=1, column=1, sticky=N)
       Label(self, text="",
             ).grid(row=2, column=1, sticky=N)
       Button(self, text="Animals", font = "Courier 20", fg="Dodger Blue",
              command=self.animal_choice
              ).grid(row=3, column=1, sticky=N)
       Label(self, text="",
             ).grid(row=4, column=1, sticky=N)
       Button(self, text="Movies", font = "Courier 20", fg="Dodger Blue",
              command=self.movie_choice
              ).grid(row=5, column=1, sticky=N)
       Label(self, text="",
             ).grid(row=6, column=1, sticky=N)
       Button(self, text="Famous People", font = "Courier 20", fg="Dodger Blue",
              command=self.famous_people
              ).grid(row=7, column=1, sticky=N)
       Label(self, text="",
             ).grid(row=8, column=1, sticky=N)


   def food_choice(self):
       text_file = open("food.txt","r")
       choice_list = []
       for line in text_file:
           line = line.strip("\n")
           choice_list.append(line)
       num = random.randint(0,len(choice_list) - 1)
       choice = choice_list[num]
       self.call_on_next(choice)

   def animal_choice(self):
       text_file = open("animals.txt", "r")
       choice_list = []
       for line in text_file:
           line.strip("\n")
           choice_list.append(line)
       num = random.randint(0, len(choice_list) - 1)
       choice = choice_list[num]
       self.call_on_next(choice)
   def movie_choice(self):
       text_file = open("movies.txt", "r")
       choice_list = []
       for line in text_file:
           line.strip("\n")
           choice_list.append(line)
       num = random.randint(0, len(choice_list) - 1)
       choice = choice_list[num]
       self.call_on_next(choice)
   def famous_people(self):
       text_file = open("famousPeople.txt", "r")
       choice_list = []
       for line in text_file:
           line = line.strip("\n")
           choice_list.append(line)
       num = random.randint(0, len(choice_list) - 1)
       choice = choice_list[num]
       self.call_on_next(choice)
   def choose(self):
       self.choose_box = Text(self, width = 20, height=4, wrap=WORD)
       Label(self, text="Enter your word or phrase here!\nSeparate your words with an underscore.\nPlease don't use any symbols in your message.\n"
                        "Ex: Harry_Potter\nWhen you're done, hit the 'Done!' Button!"
             ).grid(row=5, column=1, sticky=N)
       self.choose_box.grid(row=6, column=0, columnspan=4)
       Button(self, text="Done!",
              command=self.done
              ).grid(row=7, column=1, sticky=N)
   def done(self):
       choice = self.choose_box.get("0.0",END)
       self.call_on_next(choice)