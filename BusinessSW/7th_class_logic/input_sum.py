keep = "yes"
num = 0

while keep == "yes":
    num = int(input("숫자를 입력하시오: "))    
    keep = input("계속?(yes / no): ")
    num += num

print("합계는", num)