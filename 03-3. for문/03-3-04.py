blood = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
res = {}

for b in blood:
    if b in res:
        res[b] += 1
    else:
        res[b] = 1

print(res)
