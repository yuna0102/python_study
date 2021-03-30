import turtle
t = turtle.Turtle()
t.shape("turtle") #t.은 거북이 하나에 해당되는 일
t.speed(3)

name = turtle.textinput("", "당신의 이름은 무엇인가요? ") #터틀 그래픽 전체에 해당하는 일

for i in range(4):
    t.fd(50)
    t.left(90)

t.write("안녕하세요? %s씨, 거북이 인사드립니다!" %name)

turtle.exitonclick() 