#변수를 사용하여 사용자의 이름과 나이를 문자열 형태로 기억했다가 출력할 때 사용하는 프로그램을 작성해보자.

print("안녕하세요?")
name = input("이름이 어떻게 되시나요?: ")
length = len(name)
print("만나서 반갑습니다. %s씨" %name)
print("이름의 길이는 다음과 같군요 : %d" %length)
age = int(input("나이가 어떻게 되시나요?: "))
print("내년이면 %d이 되시는 군요" %(age+1))