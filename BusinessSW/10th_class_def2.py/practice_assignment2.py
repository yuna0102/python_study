import turtle
t = turtle.Turtle()

#n각형 입력 받아서 그리기
## n각형 정보 입력 받기
## 받은 정보로 n각형 그리기
def ready_drawing(): 
    global round_length #전역변수 선언
    number = int(turtle.textinput("", "몇 각형을 그리시겠어요?")) 
    length = int(turtle.textinput("", "한 변의 길이는?"))
    round_length = number * length #n각형 하나의 둘레 저장
    def draw_polygon(): #n각형 그리기 함수 정의
        for i in range(number):
            t.fd(length)
            t.left(360/number)
    draw_polygon() #n각형 그리기 함수 실행
    global round_sum #전역변수 선언
    round_sum += round_length
    t.write("총 누적 길이 = %d" %round_sum)

#그리기 이벤트 발생 처리
def drawit(x, y):
    t.penup()
    t.goto(x, y) #마우스 클릭 발생한 곳으로 이동
    t.pendown()
    ready_drawing() #해당 지점에서 n각형 관련 함수 실행

s = turtle.Screen() #스크린 미리 대기
round_sum = 0 #누적 둘레 초기 변수 설정
round_length = 0 #각각의 n각형 둘레 초기 변수 설정
s.onscreenclick(drawit) #스크린 위 마우스 클릭에 대한 콜백함수
s.mainloop() #그래픽 창 유지

