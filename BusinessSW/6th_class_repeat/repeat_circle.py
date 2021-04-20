import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)

for i in range(6):
    t.circle(100)
    t.left(60)

turtle.exitonclick()