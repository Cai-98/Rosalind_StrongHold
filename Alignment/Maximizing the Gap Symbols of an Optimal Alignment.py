#import numpy as np
#from math import inf 
## INPUT FILE
seq = {}
with open("D:/Download/rosalind_mgap.txt",mode='r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if '>' in line :
            t = line 
            seq[t] = ''
        else:
            seq[t] += line 
s1,s2 = seq.values()

def match(a,b):
    if a == b :return [1,0,0]
    else: return [0,1,0]

def plus(l1,l2):
    ret = []
    for i in range(3):
        ret.append(l1[i] + l2[i])
    return ret

def compare_single(l1,l2):
    m,d,g = [10,99,0.0001]
    score1 = m*l1[0] - d*l1[1] - g*l1[2]
    score2 = m*l2[0] - d*l2[1] - g*l2[2]
    if score1 > score2: return l1
    else : return l2
    '''
    if l1[2] > l2[1]: return l2
    elif l1[2] < l2[2] : return l1
    else:
        if l1[1] > l2[1]: return l2
        elif l1[1] < l2[1] : return l1
        else:
            if l1[0] >= l2[0]: return l1
            else: return l2
    '''
def compare(l1,l2,l3):
    return  compare_single(compare_single(l1,l2),l3)

blast = {}
gap = [0,0,1]
blast[(0,0)] = [0,0,0]
for i in range(1,len(s1) + 1):
    blast[(i,0)] = plus(blast[(i-1,0)],gap)
for j in range(1, len(s2) + 1):
    blast[(0,j)] = plus(blast[(0,j-1)],gap)

## [a,b,c] match dismatch gap
for i in range(1,len(s1) + 1):
    for j in range(1,len(s2) + 1):
        a,b,c = plus(blast[(i-1,j)],gap),plus(blast[(i,j-1)],gap),plus(blast[(i-1,j-1)],match(s1[i-1],s2[j-1]))
        blast[(i,j)] = compare(a,b,c)
#blast
print(blast[(len(s1),len(s2))])