import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)

#정수를 받기 전에 조건을 설정
t.up() #거북이가 그려지지 않게함
t.goto(100, 100)
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(100, 0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100, -100)
t.write("거북이가 여기로 오면 음수입니다.")

t.goto(0,0)
t.down()

num = int(turtle.textinput("", "정수를 입력해주세요")) #textinput 함수는 prompt와 출력 문자열을 필수 인자로 받는다
if num > 0 :
    t.goto(100,100)
elif num == 0 :
    t.goto(100,0)
else :
    t.goto(100, -100)

turtle.exitonclick()