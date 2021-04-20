num = int(input("정수를 입력하시오: "))

fact = 1
for i in range(1, num+1):
    fact = fact * i

print(num, "에 대한 팩토리얼 값은", fact, "이다")