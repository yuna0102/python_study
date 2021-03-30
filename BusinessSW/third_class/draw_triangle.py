#밑변과 높이가 같은 직각삼각형 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)

height = int(input("삼각형의 밑변(높이)를 입력해주세요: "))
Hypotenuse = height * (2**(1/2))
print(Hypotenuse)

t.left(45)
t.forward(Hypotenuse)
t.home()
t.forward(height)
t.left(90)
t.forward(height)

