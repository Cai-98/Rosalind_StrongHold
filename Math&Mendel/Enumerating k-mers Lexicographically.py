import random
symbols = input().split()
l = int(input())
all = len(symbols)**l
res = set()
while len(res) != all:
    s = ''
    for i in range(l):
        s += symbols[random.randint(0,len(symbols)-1)]
    res.add(s)
out = open("D:/Download/output.txt",mode='w')
res = list(res)
res.sort()
for i in res:
    out.write(i+'\n')
out.close()