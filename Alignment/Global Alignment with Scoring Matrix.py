## BLOSUM 62
BLO = {}
with open("BLOSUM62.txt",mode='r') as f:
    head = f.readline().strip('\n').split()
    num = []
    for line in f.readlines():
        num.append(line.strip('\n').split()[1:])
    for i in range(len(head)):
        for j in range(len(head)):
            BLO[(head[i],head[j])] = float(num[i][j])

import numpy as np
from math import inf 

## INPUT FILE
seq = {}
with open("D:/Download/rosalind_glob.txt",mode='r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if '>' in line :
            t = line 
            seq[t] = ''
        else:
            seq[t] += line 
s1,s2 = seq.values()

gap = -5.0
blast = np.zeros((len(s1)+1,len(s2)+1),dtype=float)
blast[0,:] = list(range(0,int(gap)*(len(s2)+1),int(gap)))
blast[:,0] = list(range(0,int(gap)*(len(s1)+1),int(gap)))
## len(s1) : row | len(s2) :col
for i in range(1,len(s1) + 1):
    for j in range(1,len(s2) + 1):
        a,b,c = blast[i-1,j]+gap,blast[i,j-1]+gap,blast[i-1,j-1]+BLO[(s1[i-1],s2[j-1])]
        blast[i,j] = max(a,b,c)
#blast
print(int(blast[-1,-1]))