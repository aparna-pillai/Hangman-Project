import turtle
from tkinter import *

class Drawing(Frame):
    def __init__(self, master):
        super(Drawing, self).__init__(master)
        self.grid()
        self.stand()
        self.head()
        self.body()
        self.arm1()
        self.arm2()
        self.leg1()
        self.leg2()
        self.eye1()
        self.eye2()
        self.mouth()

    def stand(self):
        self.t = turtle.Turtle()
        self.t.speed(5)
        self.t.setpos(0, 0)
        self.t.up()
        self.t.lt(180)
        self.t.fd(180)
        self.t.lt(90)
        self.t.fd(260)
        self.t.rt(90)
        self.t.down()
        self.t.fd(50)
        self.t.rt(180)
        self.t.fd(100)
        self.t.lt(180)
        self.t.fd(50)
        self.t.rt(90)
        self.t.fd(500)
        self.t.rt(90)
        self.t.fd(180)
        self.t.rt(90)
        self.t.fd(50)
        self.t.up()
        self.t.fd(100)
        self.t.lt(90)
        self.t.down()
        self.stand_end = self.t.pos()

    def head(self):
        self.t.setpos(self.stand_end)
        self.t.circle(50)
        self.t.rt(90)
        self.head_end = self.t.pos()

    def body(self):
        self.t.setpos(self.head_end)
        self.t.fd(200)
        self.t.rt(180)
        self.t.up()
        self.body_end = self.t.pos()

    def arm1(self):
        self.t.setpos(self.body_end)
        self.t.fd(100)
        self.t.rt(45)
        self.t.down()
        self.t.fd(100)
        self.t.up()
        self.t.rt(180)
        self.t.fd(100)
        self.t.rt(90)
        self.t.down()
        self.arm1_end = self.t.pos()

    def arm2(self):
        self.t.setpos(self.arm1_end)
        self.t.fd(100)
        self.t.up()
        self.t.rt(180)
        self.t.fd(100)
        self.t.rt(45)
        self.t.fd(100)
        self.t.rt(45)
        self.t.down()
        self.arm2_end = self.t.pos()

    def leg1(self):
        self.t.setpos(self.arm2_end)
        self.t.fd(100)
        self.t.up()
        self.t.rt(180)
        self.t.fd(100)
        self.t.rt(90)
        self.t.down()
        self.leg1_end = self.t.pos()

    def leg2(self):
        self.t.setpos(self.leg1_end)
        self.t.fd(100)
        self.t.up()
        self.t.rt(180)
        self.t.fd(100)
        self.t.rt(45)
        self.t.up()
        self.t.fd(255)
        self.t.lt(90)
        self.t.fd(20)
        self.t.down()
        self.leg2_end = self.t.pos()

    def eye1(self):
        self.t.setpos(self.leg2_end)
        self.t.circle(5)
        self.t.up()
        self.t.rt(180)
        self.t.fd(30)
        self.t.rt(90)
        self.t.fd(4)
        self.t.down()
        self.eye1_end = self.t.pos()

    def eye2(self):
        self.t.setpos(self.eye1_end)
        self.t.circle(5)
        self.t.up()
        self.t.fd(30)
        self.t.rt(180)
        self.t.down()
        self.eye2_end = self.t.pos()

    def mouth(self):
        self.t.setpos(self.eye2_end)
        self.t.circle(15, 180)
        self.t.up()
        self.t.hideturtle()

