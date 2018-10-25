a = [1, 2, 3]
b = a[:]
if a is b:
    print(True)
else:
    print(False)

'''
b=a[:]는 a의 값을 복사하여 b에 대입하는 것이기에 새로운 객체를 바라보게 되므로 False 반환
'''
