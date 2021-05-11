import random

def get_sum():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    sum = a + b
    answer = int(input("%d+%d=?" %(a, b)))
    if answer == sum:
        print ("정답입니다.")
    else:
        print ("오답입니다.")

get_sum()
get_sum()
get_sum()