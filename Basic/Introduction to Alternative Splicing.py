#from decimal import Decimal as dec
## Note: 计算组合数学问题发生Overflowerro的时候 
## 可以把结果显然是int的除法使用//
with open("D:/Download/rosalind_aspc.txt") as f:
    n , k = map(int,f.read().strip('\n').split())

def fac(n):
    res = [1]
    while len(res) <=n:
        res.append(res[-1]*len(res))
    return res[-1]
def A(n,i):
    return int(fac(n) // (fac(n-i)*fac(i)))

res = 0
for i in range(k,n+1):
    res += A(n,i)

print(int(res%1000000))