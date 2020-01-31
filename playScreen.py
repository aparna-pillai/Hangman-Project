from tkinter import *

class Play_screen(Frame):

   def __init__(self, master, choice):
       """Initialize Frame."""
       self.choice = choice
       super(Play_screen, self).__init__(master)
       master.title("Play Screen!")
       self.grid()
       self.create_widgets()

   def create_widgets(self):
       Button(self, text="A", fg = "white",bg = "navy",
              command=self.a
              ).grid(row=20, column=0, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=1, sticky=N)
       Button(self, text="B", fg="white", bg="navy",
              command=self.b
              ).grid(row=20, column=2, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=3, sticky=N)
       Button(self, text="C", fg="white", bg="navy",
              command=self.c
              ).grid(row=20, column=4, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=5, sticky=N)
       Button(self, text="D", fg="white", bg="navy",
              command=self.d
              ).grid(row=20, column=6, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=7, sticky=N)
       Button(self, text="E", fg="white", bg="navy",
              command=self.e
              ).grid(row=20, column=8, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=9, sticky=N)
       Button(self, text="F", fg="white", bg="navy",
              command=self.f
              ).grid(row=20, column=10, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=11, sticky=N)
       Button(self, text="G", fg="white", bg="navy",
              command=self.g
              ).grid(row=20, column=12, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=13, sticky=N)
       Button(self, text="H", fg="white", bg="navy",
              command=self.h
              ).grid(row=20, column=10, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=11, sticky=N)
       Button(self, text="I", fg="white", bg="navy",
              command=self.i
              ).grid(row=20, column=12, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=13, sticky=N)
       Button(self, text="J", fg="white", bg="navy",
              command=self.j
              ).grid(row=20, column=14, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=15, sticky=N)
       Button(self, text="K", fg="white", bg="navy",
              command=self.k
              ).grid(row=20, column=16, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=17, sticky=N)
       Button(self, text="L", fg="white", bg="navy",
              command=self.l
              ).grid(row=20, column=18, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=19, sticky=N)
       Button(self, text="M", fg="white", bg="navy",
              command=self.m
              ).grid(row=20, column=20, sticky=N)
       Label(self, text=""
             ).grid(row=20, column=21, sticky=N)

   def a(self):
       pass
   def b(self):
       pass
   def c(self):
       pass
   def d(self):
       pass
   def e(self):
       pass
   def f(self):
       pass
   def g(self):
       pass
   def h(self):
       pass
   def i(self):
       pass
   def j(self):
       pass
   def k(self):
       pass
   def l(self):
       pass
   def m(self):
       pass
   def n(self):
       pass
   def o(self):
       pass
   def p(self):
       pass
   def q(self):
       pass
   def r(self):
       pass
   def s(self):
       pass
   def t(self):
       pass
   def u(self):
       pass
   def v(self):
       pass
   def w(self):
       pass
   def x(self):
       pass
   def y(self):
       pass
   def z(self):
       pass