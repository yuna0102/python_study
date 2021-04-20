i = 0
j = 2

while j <= 9:
    i = 1
    while i < 9:
        print("%d * %d = %d" %(j, i+1, j*(i+1)))
        i = i + 1
    j = j + 1
