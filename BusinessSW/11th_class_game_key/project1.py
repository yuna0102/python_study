import turtle
import random

screen = turtle.Screen()
image1 = "C:/Users/USER/Desktop/python_study/rabbit.gif"
image2 = "C:/Users/USER/Desktop/python_study/turtle.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.color("pink")
t1.shape(image1)
t1.shapesize(3)
t1.pensize(5)

t2.color("blue")
t2.shape(image2)
t2.shapesize(3)
t2.pensize(5)

t1.penup()
t1.goto(-300, 0)

t2.penup()
t2.goto(-300, -100)

for i in range(100):
    d1 = random.randint(1, 60)
    t1.forward(d1)
    d2 = random.randint(1, 60)
    t2.forward(d2)
