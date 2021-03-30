import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)

n = int(input("몇 각형을 그리시겠어요?: "))
angle = 180 * (n-2) / n

for i in range(n) :
    t.fd(30)
    t.left(180 - angle)