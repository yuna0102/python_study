price = int(input("물건 값은 얼마입니까?"))

money_list = input("각각 천 원, 500원, 100원짜리를 얼마씩 갖고 있습니까?").split()
print(money_list)

money = int(money_list[0])*1000 + int(money_list[1])*500 + int(money_list[2])*100

if money >= price:
    charge = money - price
    print("음료수를 가져가세요. 잔돈은", charge, "입니다.")
else:
    need = price - money
    print("금액이 부족합니다.", need,"원을 더 넣어주세요.")