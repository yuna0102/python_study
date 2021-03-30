call_number = int(input())
call_time = input().split()

sum_Y = 0
sum_M = 0

def youngsik(t):
    j = (t // 30 ) + 1
    price = j * 10
    return price

def minsik(t):
    j = (t // 60 ) + 1
    price = j * 15
    return price

for i in range(call_number):
    time = int(call_time[i])
    Y = youngsik(time)
    M = minsik(time)
    sum_Y += Y
    sum_M += M

price_tag = { sum_Y : 'Y', sum_M : 'M' }
cheap = min(sum_Y, sum_M)


if sum_Y == sum_M :
    print('Y M',sum_Y)
elif cheap == sum_Y:
    name = price_tag[sum_Y]
    print(name, cheap )
else:
    name = price_tag[sum_M]
    print(name, cheap)

