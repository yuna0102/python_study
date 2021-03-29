def multiplication(*args):
    if type(args) == int :
        for i in args:
            i = i * i
        return i
    else : 
        print('에러발생')

print(multiplication(1,2,3))