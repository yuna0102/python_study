import random

answer = random.randint(1, 100)
guess = 0
count = 0
print("1부터 100사이의 숫자를 맞추시오.")

while guess != answer:
    guess = int(input("숫자를 입력하시오: "))
    if guess > answer:
        print("높음!")
    elif guess < answer:
        print("낮음!")
    count = count + 1

print("축하합니다. 시도횟수는 %d입니다." %count)