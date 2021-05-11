import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)

def draw_square(length):
    for i in range(4):
        t.fd(length)
        t.right(90)


for i in range(3):
    draw_square(100)
    t.up()
    t.fd(200)
    t.down()
