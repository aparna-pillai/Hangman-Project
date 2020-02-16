import tkinter
from homePage import Home_page
from instructionsPage import Instruction_page
from categoriesPage import Categories_page
from playScreen import Play_screen
from loseScreen import Lose_screen
from winScreen import Win_screen


class Hangman_Manager(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.current_screen = None

    def load_page(self):
        self.root.title("Welcome to Hangman!")
        self.current_screen = Home_page(self.root, self.instructions, self.categories)

    def instructions(self):
        self.current_screen.destroy()
        self.donald = Instruction_page(self.root, self.return_to_home)

    def return_to_home(self):
        self.donald.destroy()
        self.current_screen = Home_page(self.root, self.instructions, self.categories)

    def categories(self):
        self.current_screen.destroy()
        self.mickey = Categories_page(self.root, self.play_screen)

    def play_screen(self, choice):
        self.mickey.destroy()
        self.goofy = Play_screen(self.root, choice, self.lose_screen, self.win_screen)

    def lose_screen(self, choice):
        self.goofy.destroy()
        self.donald = Lose_screen(self.root, choice, self.play_again_for_lose, self.exit_for_lose)

    def win_screen(self):
        self.goofy.destroy()
        self.donald = Win_screen(self.root, self.play_again_for_win, self.exit_for_win)

    def play_again_for_win(self):
        self.donald.destroy()
        self.mickey = Categories_page(self.root, self.play_screen)

    def play_again_for_lose(self):
        self.donald.destroy()
        self.mickey = Categories_page(self.root, self.categories)

    def exit_for_win(self):
        self.root.destroy()

    def exit_for_lose(self):
        self.root.destroy()


def main():
    hangman = Hangman_Manager()
    hangman.load_page()
    hangman.root.mainloop()


main()
