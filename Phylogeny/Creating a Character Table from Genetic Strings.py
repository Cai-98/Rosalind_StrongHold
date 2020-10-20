import numpy as np

def judge(lst):
    slst = set(lst)
    t = ''.join(lst)
    tlst = list(slst)
    if len(slst) == 1: return False
    elif len(slst) > 2: return True
    elif (t.count(tlst[0])==1) or (t.count(tlst[1])==1):
        return False
    else:
        return True


with open("D:/Download/rosalind_cstr.txt",mode='r') as f:
    seq = f.read().split('\n')

seq = seq[:-1]
n = len(seq[0])
stable = np.zeros((len(seq),n),dtype='<U4')
for i in range(len(seq)):
    stable[i,:] = list(seq[i])

res = []
for i in range(n):
    temp = []
    poss = stable[:,i] #position of each sequence.
    if not judge(poss): continue
    ref = poss[0]
    for j in poss:
        if j == ref:
            temp.append(1)
        else:
            temp.append(0)
    res.append(temp)

with open("D:/Download/output.txt",mode='w') as f:
    for i in res:
        s = ''.join(map(str,i)) + '\n'
        f.write(s)
