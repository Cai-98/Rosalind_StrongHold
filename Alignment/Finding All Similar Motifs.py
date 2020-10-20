import time
import numpy as np
from numba import jit
#import functools
#from Bio.pairwise2 import align as al

NT = lambda : time.time()
st = NT()
with open("D:/Download/rosalind_ksim.txt",mode='r') as f:
    k = int(f.readline().strip('\n'))
    s1 = f.readline().strip('\n')
    s2 = f.readline().strip('\n')
print("Read input file..Use %s sec."%(NT()-st))
print("There are %s bp to scan"%(len(s1)))

res = []

print("Construct blast matrix..Use %s sec."%(NT()-st))

@jit(nopython=True)
def mapping():
    blast = np.zeros((len(s1)+1,len(s2)+1),dtype=np.int16)
    blast[:,0] = list(range(0,-len(s1)-1,-1))
    point = np.zeros((len(s1)+1,len(s2)+1),dtype=np.int16)

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                a = 0
            else:a = -1
            q,w,e = blast[i-1,j]-1,blast[i,j-1]-1,blast[i-1,j-1]+a
            t = max(q,w,e)
            blast[i,j] = t
            if q == t:
                point[i,j] += 1
            if w == t:
                point[i,j] += 2
            if e == t:
                point[i,j] += 4 
    return blast,point

def goback(point):
    line1 = []
    line0 = []
    for i in range(1,len(s1)+1):
        line0 = line1
        line1 = []
        #if i%10==0:print("Read %s lines..Use %s sec.."%(i,NT()-st))
        for j in range(len(s2)+1):
            if point[i,j] == 0:
                line1.append([0])
            elif i == 1:
                line1.append([j])
            elif point[i,j] == 7:
                t = list(set(line0[j-1]+line0[j]+line1[j-1]))
                line1.append(t)
            elif point[i,j] == 6:
                t = list(set(line0[j-1]+line1[j-1]))
                line1.append(t)
            elif point[i,j] == 5:
                t = list(set(line0[j-1]+line0[j]))
                line1.append(t)
            elif point[i,j] == 3:
                t = list(set(line0[j]+line1[j-1]))
                line1.append(t)
            elif point[i,j] == 4:
                t = list(set(line0[j-1]))
                line1.append(t)
            elif point[i,j] == 2:
                t = list(set(line1[j-1]))
                line1.append(t)
            elif point[i,j] == 1:
                t = list(set(line0[j]))
                line1.append(t)
        #print(line1,line0)
    return line1

blast,point = mapping()

# 回溯
print("Trace Back...Use %s sec."%(NT()-st))
'''
line0 = []
line1 = []
for ttemp in range(1,len(s1)+1):
    line0 = line1
    line1 = []
    for temp in range(len(s2)+1):
        line1.append(goback(temp,ttemp))
'''
start = goback(point)

print("Filter..Use %s sec."%(NT()-st))
score = blast[-1,:]

for s in range(len(s2)+1):
    if score[s] >= -k:
        for t in start[s]:
            if t == 0 : continue
            temp = score[s]
            new = (int(t),s-int(t)+1)
            if new in res: continue
            res.append(new)
            while temp -1 >=-k:
                p1 = (int(t)-1,s-int(t)+2)
                pw = (int(t)+1,s-int(t))
                if p1 not in res:res.append(p1)
                if pw not in res:res.append(pw)
                temp -= 1

print("result Write...")
with open("D:/Download/output.txt",mode='w') as f:
    for i in res:
        i = [str(t) for t in i]
        f.write(' '.join(i)+'\n')

print("FINISHED..Used %s"%(NT()-st))