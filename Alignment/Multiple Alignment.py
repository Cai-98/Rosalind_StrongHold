import numpy as np
import time,re, random
from Bio.pairwise2 import align as al
from Bio.pairwise2 import format_alignment
st = time.time()

seq = {}
with open("D:/Download/rosalind_mult.txt",mode='r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if '>' in line:
            s = line
            seq[s] = ''
        else:
            seq[s] += line
seq = list(seq.values())
print("read Input file..use %s"%(time.time()-st))

def get_range():
    res = set()
    while len(res) != 4*3*2:
        a = [1,2,3,0]
        res.add(tuple(sorted(a,key = lambda x: random.randint(0,100))))
    return res

def cal_score(x):
    res = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            res += al.globalms(x[i],x[j],0,-1,-1,-1)[0].score
    return res

def get_score(a,b,c,d):
    seq = [a,b,c,d]
    res = []
    for i in al.globalms(a,c,0,-1,-1,-1):
        print("dealing with {}..use {}".format(i,time.time()-st))
        sa = i.seqA
        sc = i.seqB
        for j in al.globalms(sa,d,0,-1,-1,-1):
            print("dealing with {}..use {}".format(j,time.time()-st))
            sd = j.seqB
            for k in al.globalms(sa,b,0,-1,-1,-1):
                sb = k.seqB
                res.append([sa,sb,sc,sd])
                if time.time()-st > 225: break
    max = -99999
    ret = []
    for x in res:
        sco = cal_score(x)
        if sco > max :
            max = sco
            ret = x
    return max,ret

alig = {}
for i in range(4):
    for j in range(4):
        temp = al.globalms(seq[i],seq[j],0,-1,-1,-1)
        alig[(i,j)] = temp
# 0123 0213 0312 
typeA = alig[(0,1)][0].score + alig[(2,3)][0].score
typeB = alig[(0,2)][0].score + alig[(1,3)][0].score
typeC = alig[(0,3)][0].score + alig[(1,2)][0].score
m = max(typeA,typeB,typeC)
if m == typeA:
    max_01 = -99999
    max_seq = []
    for i in alig[(0,1)]:
        a = i.seqA
        b = i.seqB
        for j in alig[(2,3)]:
            c = j.seqA
            d = j.seqB
            score,seqt = get_score(a,b,c,d)
            if score > max_01:
                max_01 = score
                max_seq = seqt
elif m == typeB:
    max_01 = -99999
    max_seq = []
    for i in alig[(0,2)]:
        a = i.seqA
        c = i.seqB
        for j in alig[(1,3)]:
            b = j.seqA
            d = j.seqB
            score,seqt = get_score(a,b,c,d)
            if score > max_01:
                max_01 = score
                max_seq = seqt
else:
    max_01 = -99999
    max_seq = []
    for i in alig[(0,3)]:
        a = i.seqA
        d = i.seqB
        for j in alig[(1,2)]:
            b = j.seqA
            c = j.seqB
            score,seqt = get_score(a,b,c,d)
            if score > max_01:
                max_01 = score
                max_seq = seqt
print(max_01)
print(max_seq)
'''
ran = list(get_range())
max = -99999
max_seq = []
for r in ran:
    temp = []
    a = al.globalms(seq[r[0]],seq[r[1]],0,-1,-1,-1)
    for i in a:
        print("dealing with {}..use {}".format(i,time.time()-st))
        seq_A = i.seqA
        seq_B = i.seqB
        b = al.globalms(seq[r[2]],seq[r[3]],0,-1,-1,-1)
        for j in b:
            print("dealing with {}..use {}".format(j,time.time()-st))
            seq_C = j.seqA
            seq_D = j.seqB
            score = get_score(seq_A,seq_B,seq_C,seq_D)
            if score[0] > max:
                max = score[0]
                max_seq = score[1]
            if time.time()-st > 225: break

sum = 0

#0,1 0,2 0,3 1,2 1,3 2,3
def get_seq(lst):
    ret = []
    for k in lst:
        for ali in alig[k]:
            ret.append(ali.seqA)
    print(ret)
    res = ''
    for i in ret:
        if len(i) > len(res):
            res = i
    return i

get_seq([(0,1),(0,2),(0,3)])
get_seq([(1,0),(1,2),(1,3)])
get_seq([(2,1),(2,0),(2,3)])
get_seq([(3,1),(3,2),(3,0)])

def status():
    res = []
    for i in range(4):
        regin = [1,1,1,1]
        regin[i] = 0
        res.append(regin)
    for i in range(4):
        for j in range(i+1,4):
            regin = [1,1,1,1]
            regin[i],regin[j] = [0,0]
            res.append(regin)
    for i in range(4):
        regin = [0,0,0,0]
        regin[i] = 1
        res.append(regin)
    res.append([1,1,1,1])
    return res

def score(s,ind):
    temp = []
    for i in range(len(s)):
        if s[i]:
            temp.append([s1,s2,s3,s4][i][ind[i]])
        else:
            temp.append('-')
    ret = blast[ind[0]-s[0],ind[1]-s[1],ind[2]-s[2],ind[3]-s[3]]
    for i in range(4):
        for j in range(i+1,4):
            if temp[i] == temp[j]:ret +=0
            else: ret -= 1
    return ret

def choose(ind):
    #max = -99999
    #stus = [1,1,1,1]
    res = []
    for s in status():
        res.append(score(s,ind))
    return max(res)
blast = np.zeros((len(s1)+1,len(s2)+1,len(s3)+1,len(s4)+1))
blast[0,0,0,:] = list(range(0,-len(s4)-1,-1))
blast[0,0,:,0] = list(range(0,-len(s3)-1,-1))
blast[0,:,0,0] = list(range(0,-len(s2)-1,-1))
blast[:,0,0,0] = list(range(0,-len(s1)-1,-1))

for q in range(1,len(s1)+1):
    for w in range(1,len(s2)+1):
        for e in range(1,len(s3)+1):
            for r in range(1,len(s4)+1):
                blast[q,w,e,r] = choose([q-1,w-1,e-1,r-1])

print(blast[-1,-1,-1,-1])
'''
print("FINISHED....use %s"%(time.time()-st))