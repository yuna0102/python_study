import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)

color_list = ['yellow', 'red', 'blue', 'green']

radious = int(input("원의 반지름은? "))
distance = int(input("원의 간격은? "))

for i in range(4):
    t.fillcolor(color_list[i])
    t.begin_fill()
    t.circle(radious)
    t.end_fill()
    t.fd(distance)

turtle.exitonclick()