import random
def jc(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s
n = int(input())
num = list(range(1,n+1))
total = pow(2,n) * jc(n)
res = set()
while len(list(res)) != total:
    lst = []
    while len(lst) != n:
        if random.randint(0,1):
            lst.append(1)
        else:
            lst.append(-1)
    temp = sorted(num,key=lambda x: random.randint(1,10))
    tt = []
    for i in range(n):
        l = str(temp[i] * lst[i])
        tt.append(l)
    res.add(' '.join(tt))

out = open("D:/Download/output.txt",mode='w')
out.write(str(total) + '\n')
for i in list(res):
    out.write(i+'\n')
out.close()