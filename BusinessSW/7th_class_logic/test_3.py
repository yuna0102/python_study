success = 0
retest = 0
fail = 0

for num in [78, 84, 97, 59, 89]:
    if num >= 80:
        success += 1
    elif num >= 60:
        retest += 1
    else:
        fail += 1

print('성공',success)
print('재시험',retest)
print('실패',fail)