H, M = map(int, input().split())
m = M - 45

def hour(H):
    if H == 0 :
        H = H + 23
    else :
        H = H - 1
    return H

def min(M, m):
    if m < 0 :
        M = m + 60
    else :
        M = m
    return M

print(hour(H), min(M, m))

