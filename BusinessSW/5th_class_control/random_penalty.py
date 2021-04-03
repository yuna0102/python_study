import random

attack_list = ['left','middle','right']
defence = random.choice(attack_list)
attack = input("공격을 어디로 하시겠습니까?: ")

if defence == attack:
    print("공격에 실패했습니다.")
else :
    print("공격에 성공했습니다.")