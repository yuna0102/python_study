import turtle
t = turtle.Turtle()


def draw_polygon():
    cumulative_sum = 0
    def get_user_input():
        number = int(turtle.textinput("", "몇 각형을 그리시겠어요?"))
        length = int(turtle.textinput("", "한 변의 길이는?"))
        cumulative_length = number * length
        return number, length, cumulative_length
    number, length, cumulative_length = get_user_input()
    for i in range(number):
        t.fd(length)
        t.left(360/number)
    t.write("총 누적 길이 = %d" %cumulative_length)
    cumulative_sum += cumulative_length
    return cumulative_sum

def drawit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_polygon()

s = turtle.Screen() 
cumulative_length = 0
s.onscreenclick(drawit)
print(cumulative_length)


s.mainloop()

