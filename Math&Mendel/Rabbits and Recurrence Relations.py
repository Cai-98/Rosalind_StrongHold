def Fib(n):
    res = [1,1]
    while len(res) < n:
        res.append(res[-1]+res[-2])
    return res[-1]
def dead (n,m):
    if n <= m:
        return 0
    else:
        return 2**(n-m-1)
def count (n,m):
    return (Fib(n) - Fib(n-m))
n , m = [int(i) for i in input().split()]
print(count(n,m))