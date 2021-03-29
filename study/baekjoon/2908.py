A, B = map(list, input().split())
A.reverse()
B.reverse()

#상수의 대답
num_A = int(A[0] + A[1] + A[2])
num_B = int(B[0] + B[1] + B[2])

print(max(num_A, num_B))