#아래의 두 개 정수를 입력 받아 터틀 그래픽으로 원을 3개 그리는 프로그램을 작성해보자.
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(10)

radius = int(input("원의 반지름: "))
distance = int(input("원의 간격: "))

for i in range(3):
    t.down() #펜 내리기
    t.circle(radius) #원을 그려주는 함수
    t.up() #펜 올리기
    t.fd(distance) #앞으로 가는 함수