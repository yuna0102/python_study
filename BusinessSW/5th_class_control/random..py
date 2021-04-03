import random
time = random.randint(1, 24) #1~24 사이의 정수값 랜덤 생성
weather = random.choice([True, False])

if (6 <= time <= 9) and weather :
    print("종달새가 노래한다")
else:
    print("종달새 목 상태 불량...")