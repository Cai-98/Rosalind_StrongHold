def fun(a, b, c, d, e, f):
    x1 = 1 * a
    x2 = 1 * b
    x3 = 1 * c
    x4 = 0.75 * d
    x5 = 0.5 * e
    x6 = 0 * f
 
    return sum([x1, x2, x3, x4, x5, x6]) * 2
 
a,b,c,d,e,f = list(map(int,input().split()))
print(fun(a,b,c,d,e,f))