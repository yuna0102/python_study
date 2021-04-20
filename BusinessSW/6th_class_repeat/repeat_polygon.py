import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)

number = int(turtle.textinput("","몇각형을 원하시나요?: "))

for i in range(number): #range 안에는 숫자가 들어가야함
    t.fd(100)
    t.left(360/number)

turtle.exitonclick()
