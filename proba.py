A, B, C, D = map(int, input().split())
tr = B - D
op = 0
if tr < 0:
    op = abs(tr)
res = A + op * C
print(res)