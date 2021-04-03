import turtle
t = turtle.Turtle()
t.shape("turtle")
t.shapesize(3, 3) #거북이 가로로 3배, 세로로 3배 움직이기
t.speed(3)

while True :
    direction = input()
    if direction == "l" :
        t.left(90)
        t.fd(100)
    else :
        t.right(90)
        t.fd(100)