import turtle
from tkinter import *
import time

class Drawing(Frame):
    def __init__(self, master):
        super(Drawing,self).__init__(master)
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


        def self.stand():
            t = turtle.Turtle()
            win = turtle.Screen()
            t.setpos(0, 0)
            t.speed(0)
            t.up()
            t.lt(180)
            t.fd(180)
            t.lt(90)
            t.fd(260)
            t.rt(90)
            t.down()
            t.fd(50)
            t.rt(180)
            t.fd(100)
            t.lt(180)
            t.fd(50)
            t.rt(90)
            t.fd(500)
            t.rt(90)
            t.fd(180)
            t.rt(90)
            t.fd(50)
            t.up()
            t.fd(100)
            t.lt(90)
            t.down()

# head
t.circle(50)

t.rt(90)

# body
t.fd(200)

t.rt(180)
t.up()

# Arm 1
t.fd(100)

t.rt(45)
t.down()
t.fd(100)
t.up()
t.rt(180)
t.fd(100)
t.rt(90)
t.down()

# Arm 2
t.fd(100)

t.up()
t.rt(180)
t.fd(100)
t.rt(45)
t.fd(100)
t.rt(45)
t.down()

# Leg 1
t.fd(100)

t.up()
t.rt(180)
t.fd(100)
t.rt(90)
t.down()

# Leg 2
t.fd(100)

t.up()
t.rt(180)
t.fd(100)
t.rt(45)
t.up()
t.fd(255)
t.lt(90)
t.fd(20)
t.down()

# Eye 1
t.circle(5)

t.up()
t.rt(180)
t.fd(30)
t.rt(90)
t.fd(4)
t.down()

# Eye 2
t.circle(5)

t.up()
t.fd(30)
t.rt(180)
t.down()

# Mouth
t.circle(15, 180)

t.up()
t.fd(100)

win.exitonclick()

