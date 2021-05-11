import turtle # turtle.shape()에서 앞의 turtle를 생략해도 되게 해줌
t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
t.pensize(2)
t.up() # 거북이기 움직일 때 선 긋기를 하지 않게 해줌
turtle.onscreenclick(goto) # 마우스를 클릭한 곳으로 거북이를 이동
x,y= t.position() # 현재 있는 곳의 좌표를 x,y에 저장
print(x,y)
def dr(x,y) : # 사각형을 그리는 함수
    t.pendown()
    print(x,y)
    for i in range(4) :
        t.fd(100),t.rt(360/4)
    t.up()
turtle.onscreenclick(dr,1,True) # 마우스 왼쪽을 클릭하면 사각형을 그리는 함수를 실행﻿
