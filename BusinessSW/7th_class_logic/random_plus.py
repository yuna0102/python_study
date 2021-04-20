import random

while True:
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    guess = int(input("%d + %d =" %(n1, n2)))
    if guess == n1 + n2:
        print("잘했어요")
    else:
        print("다음 번에는 더 잘할 수 있죠?")