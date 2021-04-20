import random

options = ['왼쪽', '중앙', '오른쪽']
success = 0
fail = 0

while True:
    computer_choice = random.choice(options)
    user_choice = input("어디를 수비하시겠어요?(왼쪽, 중앙, 오른쪽): ")
    if user_choice in options:
        if user_choice == computer_choice:
            print("수비에 성공하셨습니다.")
            success = success + 1
        else:
            print("패널티 킥이 성공하였습니다.")
            fail = fail + 1
    elif (user_choice == "q") or (user_choice == "quit"):
        break
    else:
        print("오타입니다. 다시 입력하세요.")

print("수비성공은 %d회, 실패는 %d회 입니다." %(success, fail))





