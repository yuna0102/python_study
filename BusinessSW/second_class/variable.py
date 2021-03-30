import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)

radius = 100
distance = 40
for i in range(5):
    t.circle(radius)
    t.fd(distance)