def fac(i):
    s = 1
    for j in range(1,i+1):
        s *= j
    return s

n , k = map(int,input().split())
res = int(fac(n)/fac(n-k) % 1000000)
print(res)
