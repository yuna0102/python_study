bread = ["호밀빵" , '위트', '허니오트']
meat = ['미트볼', '터키', '소시지']
vegetable = ['양상추', '토마토', '오이']
sauce = ['마요네즈', '랜치', '사우스웨스트']
sandwich = []

for i in bread:
    sandwich.append(i)
    for j in meat:
        sandwich.append(j)
        for x in vegetable:
            sandwich.append(x)
            for y in sauce:
                sandwich.append(y)
                print(sandwich)
    sandwich = []             