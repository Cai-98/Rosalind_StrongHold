from math import sqrt
A = list(map(float,input().split()))
B = []
for i in A:
    p = sqrt(i)
    res = p**2 + p*(1-p)*2
    B.append('{:.3f}'.format(res))
print(*B)