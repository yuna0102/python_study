#과제2
#5명의 학생 점수를 입력받아 리스트로 저장한 후, 무한루프를 돌면서 몇 번째 학생의 점수를 알고 싶은지 입력받아 해당 점수를 출력한다.
#만약 기록되어 있지 않은 학생의 번호가 입력되면 '없는 학번입니다. 다시 입력하세요'라고 출력한다.
#만약 99가 입력되면 프로그램 실행을 종료한다.

student_list = []

#학생 점수로 리스트 만들기
for i in range(5):
    student_score = input("%d번 학생의 점수를 입력하시오: " %(i+1))
    student_list.append(student_score)
print("입력마감\n")

#사용자가 원하는 학생의 점수 출력
while True :
    input_number = int(input("학생번호를 입력하시오: ")) 
    if input_number == 99 : 
        break #반복문 벗어나기
    elif input_number <= 5 :
        print(student_list[input_number - 1])
    else :
        print("없는 학번입니다. 다시 입력하세요.")