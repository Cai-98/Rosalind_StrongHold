def num(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s

import random
n = int(input())
t = list(range(1,n+1))
res = set()
while len(list(res)) != num(n):
    ord_t = tuple(sorted(t,key = lambda x: random.randint(1,100)))
    res.add(ord_t)
l = list(res)
print(len(res))
for i in l:
    print(*i)
