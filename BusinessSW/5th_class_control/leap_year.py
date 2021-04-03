n = int(input("숫자를 입력해주세요: "))
if ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0):
    print("leap year")
else : 
    print("NO")