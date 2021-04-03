#사용자가 입력한 기호 안에 문자열을 삽입해보자.

sign = input("기호를 입력하시오: ") #split 함수 안 써도 인덱싱으로 처리가능
#문자 철자 단위로 문자열을 쪼갬
print(sign)
middle = input("중간에 삽입할 문자열을 입력하시오: ")

print(sign[0] + middle + sign[1])