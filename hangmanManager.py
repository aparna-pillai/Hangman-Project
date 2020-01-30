import tkinter
from homePage import home_page
from instructionsPage import instruction_page
from categoriesPage import categories_page


class Hangman_Manager(object):
   def __init__(self):
       self.root = tkinter.Tk()
       self.current_screen = None

   def setup_homePage(self):
       self.root.title("Welcome to Hangman!")
       self.current_screen = home_page(self.root, self.onclose_homePage)

   def onclose_homePage(self):
       self.current_screen.destroy()


   def onclose_instructions(self):
       self.current_screen.destroy()
       categories_page.main()



   def onclose_categories(self):
        self.current_screen.destroy()

        self.setup_game()

   def setup_game(self):
       pass

def main():
   hangman = Hangman_Manager()
   hangman.setup_homePage()
   hangman.root.mainloop()


main()
