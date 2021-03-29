H, M = map(int, input().split())
m = M - 45

if H < 24 :
    if m < 0 :
        if H == 0 :
            H = H - 1 + 24
            M = m + 60
        else :
            H = H - 1
            M = m + 60
    else :
        H = H
        M = m
else :
    H = H - 24
    if m < 0 :
        M = m + 60
    else :
        M = m

print(H, M)

