#문제
#"ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

#아이디어
# 1. 문자열에 각 알파벳이 있는지 구한 후, 횟수를 센다
    # (1) if문과 in 키워드 사용 : 있는지만 알면 됨
    # (2) fine() 함수 사용 : 위치도 알아야함

#select
# 2. 문자열을 리스트로 바꾼 다음, 리스트에 해당 요소가 몇 번 등장하는 지 센다
    # (1) 문자열을 리스트로 변환 : list()
    # (2) 반환된 값에 점수 곱하기

    #map(함수, 리스트)
    #변수 = map(lambda, list)



make_list = list('ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC')
alphabet = ['A', 'B', 'C', 'D']

def count_alphabet() :
    sum = 0
    for i in alphabet :
        count = 4
        count_str = map(lambda x:x.count(i), make_list)
        list_str = list(count_str)
        count_True = list_str.count(1)
        print(count_True)
        result = count_True * count
        sum = sum + result
        count = count - 1
    return sum

print(count_alphabet())

#구글답안
# t_str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
# str_list = list(t_str)
# t = list(map(lambda c : ord('E') - ord(c) , str_list))
# print(sum(t))

#초기 아이디어
# count_a = make_list.count('A')
# count_b = make_list.count('B')
# count_c = make_list.count('C')
# count_d = make_list.count('D')

# score_A = count_a * 4
# score_B = count_b * 3
# score_C = count_c * 2
# score_D = count_d * 1
# sum = score_A + score_B + score_C + score_D
# print(sum)
