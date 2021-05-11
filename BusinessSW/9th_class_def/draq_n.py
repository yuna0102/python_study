import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)

num = int(turtle.textinput("", "몇 각형을 원하시나요?"))

def draw_n(num):
    for i in range(num):
        for i in range(num):
            t.fd(50)
            t.left(360/num)
        t.left(30)


draw_n(num)
