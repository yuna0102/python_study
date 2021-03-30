score = int(input("네 자리 정수를 입력하세요: "))
a = score // 1000
score %= 1000
b = score // 100
score %= 100
c = score // 10
score %= 10
d = score

print(a,b,c,d, a+b+c+d)