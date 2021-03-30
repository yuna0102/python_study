americano_price = 2000
latte_price = 3000
capucino_price = 3500

americano = int(input("아메리카노 판매개수"))
latte = int(input("라떼 판매개수"))
capucino = int(input("카푸치노 판매개수"))

print("총 매출은", americano*americano_price + latte*latte_price + capucino*capucino_price, "입니다")