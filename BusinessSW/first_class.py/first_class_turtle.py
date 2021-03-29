#turtle graphic
import turtle #turtle 라이브러리를 가져옴

t = turtle.Turtle() #거북이를 만드는 함수
t.shape('turtle')

for i in range(4):
    t.forward(100)
    t.left(90)

t.reset