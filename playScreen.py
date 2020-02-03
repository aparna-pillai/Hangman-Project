from tkinter import *
from turtleHangman import Drawing

class Play_screen(Frame):

    def __init__(self, master, choice):
        """Initialize Frame."""
        self.choice = str(choice)
        super(Play_screen, self).__init__(master)
        master.title("Play Screen!")
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        guess_list = []

        for letter in self.choice:
            if letter!="\n":
                guess_list.append(letter)
        let_str =""
        for item in guess_list:
            if item == "_":
                let_str +=" "

            else:
                let_str += "_ "

        Label(self,
              text=let_str, font="Courier 20 bold",
              fg="Sea Green").grid(row=1, column=1, columnspan = 1000, sticky=N)
        Label(self, text="").grid(row=2, column=1, sticky=N)

        Drawing.stand(self)
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        column = 1
        column2 = 1

        for letter in alphabet:
            if column <= 26:
                self.letter = Button(self, text=letter, fg="Medium Sea Green", bg="Gainsboro",
                                    command=self.create_letter_click_command(letter,guess_list)
                                    ).grid(row=20, column=column, sticky=N)


                Label(self, text=""
                    ).grid(row=20, column=column + 1, sticky=N)
                column += 2
            else:
                self.letter = Button(self, text=letter, fg="Medium Sea Green", bg="Gainsboro",
                                     command=self.create_letter_click_command(letter,guess_list)
                                     ).grid(row=22, column=column2, sticky=N)

                Label(self, text=""
                      ).grid(row=22, column=column2 + 1, sticky=N)

                column2 += 2
        Label(self, text=""
              ).grid(row=21, sticky=N)


    def create_letter_click_command(self,l,list):
        return lambda : self.letter_click(l,list)

    def letter_click(self,letter,list):
        self.guess_list = list
        for item in self.guess_list:
            letter_count = 0
            if item == letter:
                let_str = ""
                for item in self.guess_list:
                    pass
                Label(self,
                      text=let_str, font="Courier 20 bold", fg="Sky Blue").grid(row=1, column=1, columnspan=1000, sticky=N)

            letter_count += 1






