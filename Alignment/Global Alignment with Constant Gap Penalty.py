## BLOSUM 62
BLO = {}
with open("D:\\OneDrive - zju.edu.cn\\PTA\\BLOSUM62.txt",mode='r') as f:
    head = f.readline().strip('\n').split()
    num = []
    for line in f.readlines():
        num.append(line.strip('\n').split()[1:])
    for i in range(len(head)):
        for j in range(len(head)):
            BLO[(head[i],head[j])] = float(num[i][j])

import numpy as np
## INPUT FILE
seq = {}
with open("D:/Download/rosalind_gcon.txt",mode='r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if '>' in line :
            t = line 
            seq[t] = ''
        else:
            seq[t] += line 
s1,s2 = seq.values()
#s1 = 'MEANLY'
#s2 = 'PLEASANTLY'
gap = -5.0
blast = np.zeros((len(s1)+1,len(s2)+1),dtype=float)
blast[0,:] = [0] + [gap]*(len(s2))
blast[:,0] = [0] + [gap]*(len(s1))

for i in range(1,len(s1) + 1):
    for j in range(1,len(s2) + 1):
        t = [max(blast[:,j])+gap,max(blast[i,:])+gap,blast[i-1,j-1]+BLO[(s1[i-1],s2[j-1])]]
        m = max(t)
        blast[i,j] = m
#blast
print(int(blast[-1,-1]))