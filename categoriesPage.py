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
       Button(self, text="Animals", font="Courier 20", fg="Dodger Blue",
              command=self.animal_choice
              ).grid(row=1, column=1, sticky=N)
       Label(self, text="",
             ).grid(row=2, column=0, sticky=N)
       Button(self, text="Books", font="Courier 20", fg="Dodger Blue",
              command=self.books_choice
              ).grid(row=3, column=1, sticky=N)
       Label(self, text="",
             ).grid(row=4, column=0, sticky=N)
       Button(self, text="Famous People", font="Courier 20", fg="Dodger Blue",
              command=self.famous_people
              ).grid(row=5, column=1, sticky=N)
       Label(self, text="",
             ).grid(row=6, column=0, sticky=N)
       Button(self, text="Food", font="Courier 20", fg="Dodger Blue",
              command=self.food_choice
              ).grid(row=7, column=1, sticky=N)
       Label(self, text="",
             ).grid(row=8, column=0, sticky=N)
       Button(self, text="Movies", font="Courier 20", fg="Dodger Blue",
              command=self.movie_choice
              ).grid(row=9, column=1, sticky=N)
       Label(self, text="",
             ).grid(row=10, column=0, sticky=N)
       Button(self, text="Random", font="Courier 20", fg="Dodger Blue",
              command=self.random_choice
              ).grid(row=11, column=1, sticky=N)
       Label(self, text="",
             ).grid(row=12, column=2, sticky=N)

    def food_choice(self):
        text_file = open("food.txt", "r")
        choice_list = []
        for line in text_file:
            line = line.strip("\n")
            choice_list.append(line)
        num = random.randint(0, len(choice_list) - 1)
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
       self.call_on_next()

   def books_choice(self):
       text_file = open("books.txt", "r")
       choice_list = []
       for line in text_file:
           line = line.strip("\n")
           choice_list.append(line)
       num = random.randint(0, len(choice_list) - 1)
       choice = choice_list[num]
       self.call_on_next(choice)

   def random_choice(self):
       text_file = open("random.txt", "r")
       choice_list = []
       for line in text_file:
           line = line.strip("\n")
           choice_list.append(line)
       num = random.randint(0, len(choice_list) - 1)
       choice = choice_list[num]
       self.call_on_next(choice)
