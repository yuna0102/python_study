#과제 1
#터틀그래픽에서 도형 종류와 변의 길이(혹은 반지름), 색상을 입력받아 도형을 그린다.
# 도형의 종류는 정사각형, 정삼각형, 원 3가지 종류이고 다른 것이 입력되면 '도형을 잘못 입력했습니다.'라고 메시지를 출력한다.
# 도형 종류를 선택할 때, 정사각형 대신 4, 정삼각형 대신 3, 원 대신 0이라고 입력해도 동일하게 작동된다.

import turtle
t = turtle.Turtle()
t.shape("turtle")

figure = turtle.textinput("", "도형을 입력하시오:")
length = int(turtle.textinput("", "한 변의 길이 혹은 반지름:"))
color = turtle.textinput("", "색상을 입력하시오:")

t.fillcolor(color) #색깔 선택
t.begin_fill() #채우기 시작

if figure == ("정사각형" or "4"):
    for i in range(4):
        t.fd(length)
        t.left(90)
elif figure == ("정삼각형" or "3"):
    for i in range(3):
        t.fd(length)
        t.left(120)
elif figure == ("원" or "0"):
    t.circle(length)
else:
    t.write("도형을 잘못 입력했습니다")

t.end_fill() #채우기 종료

turtle.exitonclick() #실행 끝나도 창 닫지 않기