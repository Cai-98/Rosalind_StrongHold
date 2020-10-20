def fac(n):
    fac = 1
    if n == 0:
        return fac
    else:
        for i in range(1,n+1):
            fac = fac*i
        return fac
k , n = map(int,input().split())
person = 2**k
p = 0.25
i = 0
pp = 0
while 1:
    pp += fac(person)/(fac(i)*fac(person-i))*((1-p)**(person-i)) * (p**i)
    if i == n-1:
        break
    i += 1
ppp = 1 - pp
print('{:.3f}'.format(ppp))