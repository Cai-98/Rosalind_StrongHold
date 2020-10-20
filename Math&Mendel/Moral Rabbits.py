def f(n, k):
    s = [0] * (k + 1)  # list *4 [0, 0, 0, 0]   s[0]代表当月出生的兔子，s[k]代表当月死亡的兔子
    s[0] = 1           # [1, 0, 0, 0]
    for x in range(1, n):
        s[1:k + 1] = s[0:k]
        s[0] = sum(s[2:])
    return sum(s[:-1])

n,k = map(int,input().split())
print(f(n,k))