#사용자가 입력한 3가지 색상을 리스트에 저장했다가 하나씩 꺼내어 그 색상으로 채워진 원을 그리는 프로그램을 작성해보자.
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)

color_list = ['yellow', 'red', 'blue']
for i in range(3) :
    t.fillcolor(color_list[i])
    t.down()
    t.begin_fill() #채우기 시작 : 폐곡선이 생성될 때
    t.circle(100) #원 만들기
    t.end_fill() #채우기 끝
    t.up()
    t.fd(200)

turtle.exitonclick()

