import turtle
import math

player = turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()

def turnleft():
    player.left(5)

def turnright():
    player.right(5)

def fire():
    x = 0
    y = 0
    velocity = 50 #초기속도 50픽셀/sec
    angle = player.heading() #초기각도 heading()은 거북이 현재 방향을 리턴
    vx = velocity * math.cos(angle * 3.14 / 180.0) #도->라디안
    vy = velocity * math.sin(angle * 3.14 / 180.0) #도->라디안
    while player.ycor()>=0: #y좌표가 음수가 될 때까지. ycor()는 현재y좌표 리턴
        vx = vx #x축 방향 이동은 일정하게
        vy = vy - 10 #단위 시간당 10px 하락하도록 구현
        x = x + vx
        y = y + vy #y가 0보다 작아지면 중단
        player.goto(x, y)

#키 이벤트 처리함수 등록
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(fire, "space") #space키 누르면 fire 함수 실행
screen.listen()

turtle.exitonclick()
