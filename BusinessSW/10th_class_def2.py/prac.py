import turtle
t = turtle.Turtle()


def get_user_input():
    global cumulative_length
    number = int(turtle.textinput("", "몇 각형을 그리시겠어요?"))
    length = int(turtle.textinput("", "한 변의 길이는?"))
    cumulative_length = number * length
    def draw_polygon():
        for i in range(number):
            t.fd(length)
            t.left(360/number)
    draw_polygon()
    global cumulative_sum 
    cumulative_sum += cumulative_length
    t.write("총 누적 길이 = %d" %cumulative_sum)

def drawit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    get_user_input()

s = turtle.Screen()
cumulative_sum = 0
cumulative_length = 0
s.onscreenclick(drawit)
print(cumulative_length)
print(cumulative_sum)


s.mainloop()

