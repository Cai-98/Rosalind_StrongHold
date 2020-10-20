def par(n,m):
    if n == 0:
        return 1
    else:
        return fac(m)/(fac(n)*fac(m-n)) 

def fac(n):
    out = 1
    for i in range(1,n+1):
        out *= i
    return out
n = int(input())
res = 0
for i in range(n+1):
    res += par(i,n)
res %= 1000000
print(int(res))