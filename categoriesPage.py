from tkinter import *

class categories_page(Frame):
   def __init__(self, master,call_on_selected):
       """Initialize Frame."""
       self.call_on_selected = call_on_selected
       super(categories_page, self).__init__(master)
       self.grid()
       self.create_widgets()

   def create_widgets(self):
       Button(self, text="food",
              command=categories_page.food_choice(self,"food.txt")
              ).grid(row=2, column=0, sticky=N)
       Button(self, text="animals",
              command=categories_page.animal_choice(self,"animals.txt")
              ).grid(row=0, column=2, sticky=N)
       Button(self, text="movies",
              command=categories_page.movie_choice(self,"movies.txt")
              ).grid(row=0, column=0, sticky=N)
       Button(self, text="famous people",
              command=categories_page.famous_people(self,"famousPeople.txt")
              ).grid(row=2, column=2, sticky=N)
       Button(self, text="choose your own",
              command=categories_page.choose(self)
              ).grid(row=4, column=0, sticky=N)
       Label(self, text="         "
             ).grid(row=0, column=1, sticky=N)
       Label(self, text="         "
             ).grid(row=1, column=0, sticky=N)
       Label(self, text="         "
             ).grid(row=1, column=1, sticky=N)
       Label(self, text="         "
             ).grid(row=1, column=2, sticky=N)
       Label(self, text="         "
             ).grid(row=2, column=1, sticky=N)
       Label(self, text="         "
             ).grid(row=3, column=1, sticky=N)
       Label(self, text="         "
             ).grid(row=3, column=2, sticky=N)

   def food_choice(self,text_file):
       text_file = open(text_file,"r")
       choice_list = []
       for line in text_file:
           line.strip("\n")
           choice_list.append(line)

   def animal_choice(self,text_file):
       text_file = open(text_file, "r")
       choice_list = []
       for line in text_file:
           line.strip("\n")
           choice_list.append(line)
   def movie_choice(self,text_file):
       text_file = open(text_file, "r")
       choice_list = []
       for line in text_file:
           line.strip("\n")
           choice_list.append(line)
   def famous_people(self,text_file):
       text_file = open(text_file, "r")
       choice_list = []
       for line in text_file:
           line.strip("\n")
           choice_list.append(line)
   def choose(self):
      pass
   def main(self):
       self.create_widgets()

