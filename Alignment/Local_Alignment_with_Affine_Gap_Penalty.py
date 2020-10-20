#import numpy as np
import time,sys,re
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
from Bio.pairwise2 import format_alignment
#import multiprocessing
#from numba import jit
tt = time.time()

def deal(s):
    for i in range(len(s)):
        if re.match(r'[A-Z\-]',s[i]):
            return s[i:]

seq = {}
with open("D:/Download/rosalind_laff.txt",mode='r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if '>' in line :
            t = line 
            seq[t] = ''
        else:
            seq[t] += line 
s1,s2 = seq.values()
r1,r2 = [{},{}]
print('Time used(input file read): {} sec'.format(time.time()-tt))
print("their are {},{} lines for two files...".format(len(s1),len(s2)))

bol = matlist.blosum62
for a in pairwise2.align.localds(s1,s2,bol,-11,-1):
    b = format_alignment(*a,full_sequences=False)
    break

with open("D:/Download/output.txt",mode='w') as f:
    r1,_,r2,score,_1 = b.split('\n')
    r1,r2 = map(deal,[r1,r2])
    r1 = r1.replace('-','')
    r2 = r2.replace('-','')
    score = score[8:]
    f.write(score+'\n' + r1+'\n' + r2)


sys.exit(print('Time used(Whole program): {} sec'.format(time.time()-tt)))

'''
@jit
def choose(c,d):#choose(a,b,c,d,ls)
    res = max(c,d)
    rw,cl = ls
    if a == res: # s1 gap
        r1[(i,j)] = r1.get((rw,j),'') + s1[int(rw):int(i)]
        r2[(i,j)] = r2.get((rw,j),'') + '-'*int(i-rw)
    elif b == res: # s2 gap
        r1[(i,j)] = r1.get((i,cl),'') + '-'*int(j-cl)
        r2[(i,j)] = r2.get((i,cl),'') + s2[int(cl):int(j)]
    elif c == res: # 匹配或突变
        r1[(i,j)] = r1.get((i-1,j-1),'') + s1[i-1]
        r2[(i,j)] = r2.get((i-1,j-1),'') + s2[j-1]
    elif d == res:
        r1[(i,j)] = ''
        r2[(i,j)] = ''
    return res
remi = {}
def gapi(row,col):
    max = blast[row-1,col] - 11
    rw = row - 1
    start = remi.get(col,0)
    for k in range(start,row):
        score = blast[k,col] - 11 - (row - k - 1)
        if score > max:
            max = score
            rw = k
    remi[col] = rw
    return max,rw

remj = {}
def gapj(row,col):
    max = blast[row,col-1] - 11
    cl = col -1
    start = remj.get(row,0)
    for k in range(start,col):
        score = blast[row,k] - 11 - (col - k - 1)
        if score > max:
            max = score
            cl = k
    remj[row] = cl
    return max,cl

## BLOSUM 62
BLO = {}
with open("D:/OneDrive - zju.edu.cn/PTA/BLOSUM62.txt",mode='r') as f:
    head = f.readline().strip('\n').split()
    num = []
    for line in f.readlines():
        num.append(line.strip('\n').split()[1:])
    for i in range(len(head)):
        for j in range(len(head)):
            BLO[(head[i],head[j])] = float(num[i][j])
print('Time used(Blosum62 read): {} sec'.format(time.time()-tt))


#seq = {}
blast = np.zeros((len(s1)+1,len(s2)+1))

for i in range(1,len(s1) + 1):
    if i%500==0:print("Read %s No.line"%i);print("Time have used {} sec".format(time.time()-tt))
    for j in range(1,len(s2) + 1):
        #b1,rw = gapi(i,j)
        #b2,cl = gapj(i,j)
        #blast[i,j] = choose(b1,b2,blast[i-1,j-1]+BLO[(s1[i-1],s2[j-1])],0,[rw,cl])
        blast[i,j] = choose(blast[i-1,j-1]+BLO[(s1[i-1],s2[j-1])],0)

print('Time used(blasting): {} sec'.format(time.time()-tt))
'''
