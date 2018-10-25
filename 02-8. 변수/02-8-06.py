a = [1,2,3]
print(id(a))
a = a + [4,5]
print(a)
print(id(a))

b = [1,2,3]
print(id(b))
b.extend([4,5])
print(b)
print(id(b))

'''
+ 기호를 이용해 더한 경우는 a의 리스트 값이 변하는 것이 아니라 두 리스트가 더해진 새로운 리스트가 리턴 되는 것
extend를 이용하면 b리스트에 값을 추가하는 것으로 b 리스트가 리턴되는 것
'''
