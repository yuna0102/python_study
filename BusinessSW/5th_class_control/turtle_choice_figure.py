import turtle
t = turtle.Turtle()
t.shape("turtle")
t.shapesize(3, 3)
t.speed(3)

figure = turtle.textinput("", "어떤 도형을 그리시겠습니까?")

if figure == "사각형":
    hor = int(turtle.textinput("", "가로 길이는?"))
    ver = int(turtle.textinput("", "세로 길이는?"))
    for i in range(2):
        t.fd(hor)
        t.left(90)
        t.fd(ver)
        t.left(90)
elif figure == "삼각형":
    hor = int(turtle.textinput("", "한 변의 길이는?"))
    for i in range(3):
        t.fd(hor)
        t.left(120)
elif figure == "원":
    hor = int(turtle.textinput("", "원의 반지름은?"))
    t.circle(hor)
else:
    print("삼각형, 사각형, 원 중에 하나를 선택해주십시오")