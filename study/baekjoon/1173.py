N, m, M, T, R = map(int, input().split()) #N은 운동횟수, m은 최소맥박, M은 최대맥박, T는 증가맥박, R은 감소맥박

X = m
n = 0
count = 0

while True:
    if X + T <= M :
        X = X + T
        n += 1
        count += 1
        if n == N:
            break
    else:
        X = X - R
        count += 1
    

print(count)

