multiple_12 = 0
multiple_3 = 0
multiple_4 = 0
multiple_none = 0
total = 0

while total < 5:
    user_input = int(input("정수를 입력하시오 : "))
    if (user_input % 3 == 0) and (user_input % 4 == 0):
        print("%d은(는) 3과 4의 공배수입니다." %user_input)
        multiple_12 += 1 
    elif user_input % 3 == 0:
        print("%d은(는) 3만의 배수입니다." %user_input)
        multiple_3 += 1 
    elif user_input % 4 == 0:
        print("%d은(는) 4만의 배수입니다." %user_input)
        multiple_4 += 1 
    else:
        print("%d은(는) 3 또는 4의 배수가 아닙니다." %user_input)
        multiple_none += 1 
    total += 1

print("3만의 배수는 %d개, 4만의 배수는 %d개, 3과 4의 공배수는 %d개 입니다." %(multiple_3, multiple_4, multiple_12))