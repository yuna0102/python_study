plain_text = "Love will find a way"

#암호화 과정
encryped_text = ""
for c in plain_text:
    x = ord(c)  #글자의 코드 값을 구한 후
    x = x + 1   #코드 값을 하나 더해
    cc = chr(x) #그에 해당하는 문자를
    encryped_text = encryped_text + cc  #암호문에 추가한다.

print(encryped_text)