from tkinter import *
from turtleHangman import Drawing, win


class Play_screen(Frame):
    def __init__(self, master, choice, return_home, return_to_home):
        """Initialize Frame."""
        self.choice = str(choice)
        self.return_home = return_home
        self.return_to_home = return_to_home
        super(Play_screen, self).__init__(master)
        master.title("Play Screen!")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.let_str = []
        self.bodypartcount = 0
        self.guess_list = []

        for letter in self.choice:
            if letter != "\n":
                self.guess_list.append(letter)

        for item in self.guess_list:
            if item !="_":
                self.let_str.append("_")
            else:
                self.let_str.append(" ")

        Drawing.stand(self)

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        column = 1
        column2 = 1
        self.guess_label = Label(self,
                                 text=" ".join(self.let_str), font="Courier 20 bold",
                                 fg="Sea Green"
                                 )
        self.guess_label.grid(row=1, column=1, columnspan=1000, sticky=N)
        Label(self, text=" ").grid(row=2, column=1, sticky=N)

        self.letter_button_dict = {}
        self.let_str_list = []

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
                self.letter_button_dict[letter] = Button(self, text=letter, fg="Medium Sea Green", bg="Gainsboro",
                                     command=self.create_letter_click_command(letter)
                                     )

                self.letter_button_dict[letter].grid(row=22, column=column2, sticky=N)

                Label(self, text=""
                      ).grid(row=22, column=column2 + 1, sticky=N)

                column2 += 2
        Label(self, text=""
              ).grid(row=21, sticky=N)

    def create_letter_click_command(self, l):
        self.bodypartcount = 0
        return lambda: self.letter_click(l)

    def letter_click(self,letter):
        count_var = 0
        other = 0
        self.letter_button_dict[letter]["state"] = DISABLED
        for num in range(len(self.guess_list)):
            if letter == self.guess_list[num]:
                self.let_str[num] = self.guess_list[num]
                self.guess_label['text'] =" ".join(self.let_str)
                # is_letter_in_word = True
            else:
                count_var += 1

        if count_var == len(self.guess_list):
            self.bodypartcount += 1
            self.remove_body_part()

        for char in self.let_str:
            if char != "_":
                other += 1

        if self.bodypartcount == 9 or other == len(self.let_str):
            self.back_to_home()

    def remove_body_part(self):
        if self.bodypartcount == 1:
            Drawing.head(self)
        elif self.bodypartcount == 2:
            Drawing.body(self)
        elif self.bodypartcount == 3:
            Drawing.arm1(self)
        elif self.bodypartcount == 4:
            Drawing.arm2(self)
        elif self.bodypartcount == 5:
            Drawing.leg1(self)
        elif self.bodypartcount == 6:
            Drawing.leg2(self)
        elif self.bodypartcount == 7:
            Drawing.eye1(self)
        elif self.bodypartcount == 8:
            Drawing.eye2(self)
        elif self.bodypartcount == 9:
            Drawing.mouth(self)

    def back_to_home(self):
        if self.bodypartcount == 9:
            self.return_home(self.choice)
        else:
            self.return_to_home()