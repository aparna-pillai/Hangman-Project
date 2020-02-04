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
            if letter != "\n":
                guess_list.append(letter)
        let_str = ""
        for item in guess_list:
            if item == "_":
                let_str += " "

            else:
                let_str += "_ "


        Drawing.stand(self)
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        column = 1
        column2 = 1
        string = ""
        self.guess_label = Label(self,
                                 text=let_str, font="Courier 20 bold",
                                 fg="Sea Green"
                                 ).grid(row=1, column=1, columnspan=1000, sticky=N)
        Label(self, text="").grid(row=2, column=1, sticky=N)
        for letter in alphabet:
            if column <= 26:
                self.letter = Button(self, text=letter, fg="Medium Sea Green", bg="Gainsboro",
                                     command=self.create_letter_click_command(letter,guess_list, string)
                                     ).grid(row=20, column=column, sticky=N)

                Label(self, text=""
                      ).grid(row=20, column=column + 1, sticky=N)

                column += 2
            else:
                self.letter = Button(self, text=letter, fg="Medium Sea Green", bg="Gainsboro",
                                     command=self.create_letter_click_command(letter,guess_list, string)
                                     ).grid(row=22, column=column2, sticky=N)

                Label(self, text=""
                      ).grid(row=22, column=column2 + 1, sticky=N)

                column2 += 2
        Label(self, text=""
              ).grid(row=21, sticky=N)


    def create_letter_click_command(self, l, list, string):
        return lambda: self.letter_click(l, list, string)

    def letter_click(self, letter, list, string):
        self.guess_list = list  # all the letters in the player's choice
        self.let_str = string
        self.totalcount = 1
        self.bodypartcount = 0

        for item in self.guess_list:
            if letter != item:
                self.let_str += "_ "
            else:
                self.totalcount = 0
                self.let_str += letter

        if self.totalcount == 1:
            pass

# GO TO TURTLEHANGMAN.PY AND FINISH WRITING THE FUNCTIONS.

# WHAT DEF LETTER_CLICK DOES IS IT TAKES THE LETTER THAT THE USER CHOSE AND COMPARES EVERY ITEM IN
# THE GUESS_LIST (GUESS_LIST CONTAINS ALL THE LETTERS OF THE WORD THEY HAVE TO GUESS) TO THE LETTER THAT THEY CHOSE.

# IF THE LETTER ISN'T EQUAL TO ONE OF THE LETTERS IN THE LIST, THEN IT TAKES A STRING AND ADDS A BLANK TO IT ("_")

# IF THE LETTER IS EQUAL TO TO ONE OF THE LETTERS IN THE LIST, IT ADDS THAT LETTER TO THE STRING. IT ALSO
# MAKES SELF.TOTALCOUNT = 0

# NOTE THAT SELF.TOTALCOUNT EQUALS ONE AT FIRST. IF AT THE END OF THE ENTIRE FOR LOOP, SELF.TOTALCOUNT ISN'T EQUAL TO 0,
# THAT MEANS THAT THE USER'S GUESS IS WRONG.

# IF IT IS, THEN IT GOES TO THE STATEMENT "IF SELF.TOTALCOUNT == 1:"

# IN THIS STATEMENT, WE HAVE TO CALL ONE OF THE FUNCTIONS IN TURTLEHANGMAN.PY SO THAT A BODY PART IS DRAWN.

# MAKE SURE THAT YOU GUYS WRITE IT SO THAT EACH TIME THE USER MESSES UP A GUESS, A different BODY PART IS ADDED.


# APARNA/ADITI: ASK MR.WANG WHY THE BELOW LINE DOESN'T REPLACE THE TEXT IN THE LABEL

        self.guess_label["text"] = self.let_str

"""I think I actually had a problem like this, but I forgot what I did."""
"""I might have solved it by defining the label for the first time later. Maybe don't define guess_label
    earlier -- define it now instead. --Aditi"""
# AFTER YOU ARE DONE WITH THAT, YOU GUYS CAN CONTINUE WORKING ON THE CODE. WE STILL HAVE THE PROBLEM THAT I SHOWED YOU GUYS THIS MORNING!!

"""What problem?"""

        #Label(self,
              #text=self.let_str, font="Courier 20 bold", fg="Sea Green").grid(row=1, column=1, columnspan=1000,
                                                                              #sticky=N)








