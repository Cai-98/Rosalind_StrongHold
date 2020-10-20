## PAM 250
PAM = {}
with open("D:\\OneDrive - zju.edu.cn\\PTA\\PAM250.txt",mode='r') as f:
    head = f.readline().strip('\n').split()
    num = []
    for line in f.readlines():
        num.append(line.strip('\n').split()[1:])
    for i in range(len(head)):
        for j in range(len(head)):
            PAM[(head[i],head[j])] = float(num[i][j])

import numpy as np
#import copy
#from math import inf 

## INPUT FILE
seq = {}
with open("D:/Download/rosalind_loca.txt",mode='r') as f:
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

record = {}
## function record the chose
def select(a,b,c,d):
    ret = max(a,b,c,d)
    if ret == 0:
        record[(i,j)] = []
    elif ret == a:
        record[(i,j)] = record[(i-1,j)] + [(i-1,j)]
    elif ret == b:
        record[(i,j)] = record[(i,j-1)] + [(i,j-1)]
    elif ret == c:
        record[(i,j)] = record[(i-1,j-1)] + [(i-1,j-1)]
    return ret

## Alignment
for i in range(1,len(s1) + 1):
    for j in range(1,len(s2) + 1):
        a,b,c = blast[i-1,j]+gap,blast[i,j-1]+gap,blast[i-1,j-1]+PAM[(s1[i-1],s2[j-1])]
        blast[i,j] = select(a,b,c,0)

with open("D:/Download/out.txt",mode='w') as f:
    ind = np.where(blast == np.max(blast))
    i0,i1 = ind[0][0],ind[1][0]
    f.write(str(int(blast[i0,i1]))+ '\n')
    temp = record[i0,i1]
    a,b = temp[0][0],temp[-1][0]
    c,d = temp[0][1],temp[-1][1]
    f.write(s1[a:b+1]+'\n')
    f.write(s2[c:d+1])