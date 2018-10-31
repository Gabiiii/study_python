inp = "나이:30,키:180"

temp = inp.split(",")
age = int(temp[0].split(":")[-1])
heigh = int(temp[1].split(":")[-1])

'''
age = 30
heigh = 180
'''

if age < 30 and heigh >= 175:
    print("Yes")
else:
    print("No")
