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
        self.let_str = ""
        self.bodypartcount = 0
        self.guess_list = []

        for letter in self.choice:
            if letter != "\n":
                self.guess_list.append(letter)

        for item in self.guess_list:
            if item == "_":
                self.let_str += " "

            else:
                self.let_str += "_ "

        Drawing.stand(self)

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        column = 1
        column2 = 1
        self.guess_label = Label(self,
                                 text=self.let_str, font="Courier 20 bold",
                                 fg="Sea Green"
                                 ).grid(row=1, column=1, columnspan=1000, sticky=N)
        Label(self, text="").grid(row=2, column=1, sticky=N)

        self.letter_button_dict = {}

        for letter in alphabet:
            if column <= 26:
                self.letter_button_dict[letter] = Button(self, text=letter, fg="Medium Sea Green", bg="Gainsboro",
                                                         command=self.create_letter_click_command(letter)
                                                         )
                self.letter_button_dict[letter].grid(row=20, column=column, sticky=N)

                Label(self, text=""
                      ).grid(row=20, column=column + 1, sticky=N)

                column += 2
            else:
                self.letter = Button(self, text=letter, fg="Medium Sea Green", bg="Gainsboro",
                                     command=self.create_letter_click_command(letter)
                                     ).grid(row=22, column=column2, sticky=N)

                Label(self, text=""
                      ).grid(row=22, column=column2 + 1, sticky=N)

                column2 += 2
        Label(self, text=""
              ).grid(row=21, sticky=N)

    def create_letter_click_command(self, l):
        return lambda: self.letter_click(l)

    def letter_click(self, letter):
        self.tries = 0

        for item in self.guess_list:
            if letter != item:
                my_list = []
                for char in self.let_str:
                    my_list.append(char)
                    for thing in my_list:
                        if thing != "_":
                            self.let_str += thing
                        elif thing == "_":
                            self.let_str += "_ "

            else:
                self.let_str += letter
                self.tries += 1
        print(self.guess_list)

        if self.tries == 0:
            self.bodypartcount += 1
            (self.letter_button_dict[letter])["state"] = DISABLED

        Label(self,
              text=self.let_str, font="Courier 20 bold", fg="Sea Green").grid(row=1, column=1, columnspan=1000,
                                                                              sticky=N)

    def remove_body_part(self):
        if self.bodypartcount == 1:
            Drawing.head(self)
        if self.bodypartcount == 2:
            Drawing.body(self)
        if self.bodypartcount == 3:
            Drawing.arm1(self)
        if self.bodypartcount == 4:
            Drawing.arm2(self)
        if self.bodypartcount == 5:
            Drawing.leg1(self)
        if self.bodypartcount == 6:
            Drawing.leg2(self)
        if self.bodypartcount == 7:
            Drawing.eye1(self)
        if self.bodypartcount == 8:
            Drawing.eye2(self)
        if self.bodypartcount == 9:
            Drawing.mouth(self)

        # self.guess_label["text"] = self.let_str
