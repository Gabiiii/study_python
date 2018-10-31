num = 1
res = 0

while num <= 1000:
    if num % 3 == 0:
        res += num
    num += 1

print(res)
