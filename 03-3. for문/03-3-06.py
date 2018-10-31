rem = ['a', 'e', 'i', 'o', 'u']
A = "Life is too short, you need python"

res = ''.join([r for r in A if r not in rem])
print(res)
