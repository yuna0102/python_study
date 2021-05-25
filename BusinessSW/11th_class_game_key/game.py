import turtle
import random

player = turtle.Turtle()

player.color("blue")
player.shape("turtle")
player.penup()        # 날아다니므로 흔적을 남기지 말아야 한다.
player.speed(0)      # 최대한 빠르게 

# 이벤트 처리를 위해 스크린 객체를 얻는다.
screen = player.getscreen()     #거북이가 있는 스크린의 이름을 알려줘

# 소행성을 두 개 만들어 랜덤하게 위치시킨다. 
a1 = turtle.Turtle()
a1.color("red")
a1.shape("circle")
a1.penup()
a1.speed(0)
a1.goto(random.randint(-300, 300), random.randint(-300, 300))

a2 = turtle.Turtle()
a2.color("red")
a2.shape("circle")
a2.penup()
a2.speed(0)
a2.goto(random.randint(-300, 300), random.randint(-300, 300))

# 이벤트 처리함수 정의
def turnleft():
     player.left(30)     # 왼쪽으로 30도 회전한다.

def turnright():
     player.right(30)   # 오른쪽으로 30도 회전한다.

# 이벤트 처리함수 등록
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.listen() #screen을 보고 있다가 감지함

def play():
     player.forward(2)     # 2픽셀 전진
     a1.forward(2)
     a2.forward(2)
     screen.ontimer(play, 10)      # 10ms가 지나면 play()를 다시 호출

screen.ontimer(play, 10)

turtle.exitonclick()