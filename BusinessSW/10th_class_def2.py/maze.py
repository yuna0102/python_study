import turtle
import random

#미로 그리는 함수
def draw_maze(x, y):
    for i in range(2):
        t.penup()
        if i == 1:
            t.goto(x+100, y+100)
        else:
            t.goto(x, y)
        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)

#좌우 화살표시 이벤트 처리 함수 정의  
def turn_left():
    t.left(10)
    t.forward(10)

def turn_right():
    t.right(10)
    t.forward(10)

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(3)

draw_maze(-300, 200)
screen.onkey(turn_left, "Left") #left키가 눌러지면 turn_left()를 실행
screen.onkey(turn_right, "Right") #right키가 눌러지면 turn_right()를 실행

#출발지점으로 온다.
t.penup()
t.goto(-300, 250)
t.speed(3)
t.pendown()

#이벤트를 기다리다 처리한다.
screen.listen() #키보드 입력을 감지하면 onkey()에 전달해 작업을 시킨다.
screen.exitonclick()