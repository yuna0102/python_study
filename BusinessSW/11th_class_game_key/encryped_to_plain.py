# 암호문
encryped_text = 'Mpwf!xjmm!gjoe!b!xbz/'

# 복호화 과정
plain_text = "" 				
for c in encryped_text:
    x = ord(c)		# 글자의 코드 값을 구한 후
    x = x - 1		# 코드 값을 하나 감소시켜
    cc = chr(x)		# 그에 해당하는 문자를
    plain_text = plain_text + cc    # 평문에 추가한다.

print(plain_text) 
