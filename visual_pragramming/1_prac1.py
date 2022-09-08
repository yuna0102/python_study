#모든 스펠링은 대문자로 쓰면 상수로 이해

from tkinter import CURRENT, N


ORIGIN = 24
RATE = 0.06
N = int(input("예금한 지, 몇 년이 경과했는가?"))
CURRENT = 60000000000

x = ORIGIN*(1 + RATE)**N

if x >= CURRENT:
    print("팔지 않는 것이 더 이득입니다.")
else:
    print("파는 것이 이득입니다.")