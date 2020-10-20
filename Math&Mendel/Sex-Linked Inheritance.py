
A = list(map(float,input().split()))
B = [2*i*(1-i) for i in A]
print(*B)