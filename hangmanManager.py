import tkinter
from homePage import Home_page
from instructionsPage import Instruction_page
from categoriesPage import Categories_page
from playScreen import Play_screen
from loseScreen import Lose_screen


class Hangman_Manager(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.current_screen = None

    def load_page(self):
        self.root.title("Welcome to Hangman!")
        self.current_screen = Home_page(self.root, self.call_next, self.other_call_next)

    def call_next(self):
        self.current_screen.destroy()
        self.donald = Instruction_page(self.root, self.return_to_home)

    def return_to_home(self):
        self.donald.destroy()
        self.current_screen = Home_page(self.root, self.call_next, self.other_call_next)

    def other_call_next(self):
        self.current_screen.destroy()
        self.mickey = Categories_page(self.root, self.call_for_main_game)

    def call_for_main_game(self, choice):
        self.mickey.destroy()
        self.goofy = Play_screen(self.root, choice, self.lose_screen)

    def lose_screen(self, pick):
        self.goofy.destroy()
        self.daisy = Lose_screen(self.root, self.done)

    def done(self):
        pass


def main():
    hangman = Hangman_Manager()
    hangman.load_page()
    hangman.root.mainloop()


main()
