import turtle

t = turtle.Turtle()
t.speed(3)

for i in range(3):
    t.fd(100)
    t.left(120)

t.penup()
t.fd(200) #t.goto(200, 0) : 좌표값으로 이동
t.pendown()

for i in range(4):
    t.fd(100)
    t.left(90)