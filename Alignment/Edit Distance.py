import numpy as np
import copy

IN = open("D:/Download/rosalind_edit.txt",mode='r')
seq = {}
for line in IN.readlines():
    line = line.strip('\n')
    if '>' in line :
        t = line
        seq[t] = ''
    else:
        seq[t] += line
IN.close()
s1, s2 = seq.values()

n , m = len(s1),len(s2)
D = [[]]
temp = [0] * (n+1)
for k in range(n+1):
    D[0].append(k)
for k in range(m):
    temp[0] += 1
    D.append(copy.deepcopy(temp))

for y in range(1,m+1):
    for x in range(1,n+1):
        if s1[x-1] == s2[y-1]:
            a = 0
        else:
            a = 1
        D[y][x] = min(D[y-1][x]+1,D[y][x-1]+1,D[y-1][x-1]+a)
print(np.array(D))
with open("D:/Download/test.txt",mode='w') as f:
    for line in D:
        line = [str(i) for i in line]
        f.write('\t'.join(line)+'\n')