import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

size = int(input("집의 크기는 얼마로 할까요? "))
for i in range(4):
    t.forward(size)
    t.right(90)
t.left(60)
for i in range(3):
    t.forward(size)
    t.right(120)