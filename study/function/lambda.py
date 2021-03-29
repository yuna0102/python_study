#람다는 '기능'을 매개변수로 전달
# 1. map 함수 : map(함수, 리스트)-> list에 있는 item들을 한 번씩 함수에 대입해 리스트로 출력
# 2. filter 함수 : filter(함수, 리스트)-> list에 있는 item들읋 함수에 대입하는데, 이때 return값이 True인 것만 모아서 리스트로 출력

lambdas = [lambda x,y:x+y, lambda x,y:x*y]
print(lambdas[0](5, 8))
print(lambdas[1], (5,8))