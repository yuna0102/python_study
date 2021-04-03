import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)

xy_list = []
xy_list.append(int(input("x1:")))
xy_list.append(int(input("x2:")))
xy_list.append(int(input("x3:")))
xy_list.append(int(input("y1:")))
xy_list.append(int(input("y2:")))
xy_list.append(int(input("y3:")))

#append로 list에 넣고 index로 빼내는 것
t.goto(xy_list[0], xy_list[3]) #goto는 설정한 x,y좌표로 이동
t.goto(xy_list[1], xy_list[4])
t.goto(xy_list[2], xy_list[5])
