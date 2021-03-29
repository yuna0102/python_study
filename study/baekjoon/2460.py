train = []
sum_list = []

for i in range(10) :
    numbers = list(map(int, input().split()))
    train.append(numbers)

sum = 0
for i in range(10) :
    sum = sum - train[i][0] + train[i][1]
    sum_list.append(sum)

print(max(sum_list))
