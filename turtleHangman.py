import turtle
import time

t = turtle.Turtle()
win = turtle.Screen()
t.speed(0)

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
t.circle(5)
t.up()
t.rt(180)
t.fd(20)
t.down()
t.circle(5)


win.exitonclick()
