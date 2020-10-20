In = open("D:/Download/rosalind_mmch.txt",mode='r')
_ = In.readline()
s = ''
for line in In.readlines():
    s += line.strip('\n')
In.close()

A = s.count('A')
U = s.count('U')
G = s.count('G')
C = s.count('C')

def mat(a,b):
    if a > b:
        a,b = b,a 
    return fac(b)//fac(b-a)

def fac(n):
    S = 1
    for i in range(1,n+1):
        S *= i
    return S
res = mat(A,U) * mat(C,G)
print(int(res))