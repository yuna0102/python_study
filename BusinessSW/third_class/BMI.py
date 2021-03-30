#BMI 계산하기
weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))

BMI = weight / (height ** 2)
print(BMI)