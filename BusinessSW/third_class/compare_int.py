x = int(input("x값은? "))
y = int(input("y값은? "))

sum = x + y
minus = x - y
multiple = x * y
big = max(x, y) #인자들을 비교해서 큰 값을 추출
small = min(x, y) #인자들을 비교해서 작은 값을 추출
print(sum, minus, multiple, big, small)