A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
res = 0

while A:
    chk = A.pop()
    if chk >= 50:
        res += chk

print(res)
