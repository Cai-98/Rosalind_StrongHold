import numpy as np
import time
from math import inf
#from copy import deepcopy as dpc
from Bio.pairwise2 import align as al

NT = lambda : time.time()
st = NT()
seq = {}
with open("D:/Download/rosalind_osym.txt",mode='r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if '>' in line:
            s = line
            seq[s] = ''
        else:
            seq[s] += line
s1,s2 = seq.values()
print("READ INPUT FILES...USE %s sec."%(NT()-st))

def get_score(a,b):
    if a == b:return 1
    else: return -1

def memo_pair(s1,s2):
    T = np.zeros((len(s1),len(s2)))
    T[0,:] = list(range(0,-len(s2),-1))
    T[:,0] = list(range(0,-len(s1),-1))
    for i in range(1,len(s1)):
        for j in range(1,len(s2)):
            q,w,e = T[i-1,j]-1,T[i,j-1]-1,T[i-1,j-1]+get_score(s1[i-1],s2[j-1])
            T[i,j] = max(q,w,e)
    return T
A = memo_pair(s1,s2)
C = memo_pair(s1[::-1],s2[::-1])
def set_point(x,y): 
    a = A[x,y]
    c = C[len(s1)-1-x,len(s2)-y-1]
    b = 1 if s1[x] == s2[y] else -1
    score = a + b + c
    if score > M[x,y]:
        M[x,y] = score
M = -inf*np.ones((len(s1),len(s2)))
for i in range(len(s1)):
    for j in range(len(s2)):
        set_point(i,j)
        if i%10 == 0:print("set {} {}.Use {}".format(i,j,NT()-st))
#
print(int(M[-1,-1]))
print(int(np.sum(M)))