res = []

for i in range(10) :
    out_p, in_p = map(int, input().split())
    sum = in_p - out_p
    res.append(sum)

print(max(res))    
