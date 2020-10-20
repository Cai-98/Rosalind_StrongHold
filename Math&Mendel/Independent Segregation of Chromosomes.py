from math import log10 
from math import factorial as fac
from decimal import Decimal as dec
log = lambda x: dec(log10(x))
N = int(input()) * 2
A = [0] *(N+1)
#A[0] = N * 0.5 ** N
for i in range(1,N+1):
    A[i] = dec(A[i-1]) + dec(0.5 ** N) * (dec(fac(N))/(dec(fac(N-i+1))*dec(fac(i-1))))

A = [dec(log(1-A[i])) for i in range(1,N+1)]
res = []
for i in A:
    s = '{:.3f}'.format(i)#int(i*10000+dec(0.5))/10000
    res.append(s)
print(*res)