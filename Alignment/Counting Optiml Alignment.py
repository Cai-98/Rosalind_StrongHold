import numpy as np

seq = {}
with open("D:/Download/rosalind_ctea.txt",mode='r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if '>' in line :
            t = line 
            seq[t] = ''
        else:
            seq[t] += line 
s1,s2 = seq.values()
res = np.zeros((len(s1)+1,len(s2)+1))
res[0,:] = [1] * (len(s2) + 1)
res[:,0] = [1] * (len(s1) + 1)
MOD = 2**27 - 1

def choose(a,b,c):
    ret = min(a,b,c)
    inp = [a,b,c]
    flag = [0,0,0]
    for k in range(3):
        if inp[k] == ret:
            flag[k] = 1
    for k in range(3): 
        if not flag[k]:
            if k == 0: # 
                res[i,j] = res[i-1,j]
            if k == 1: # 
                res[i,j] = res[i,j-1]
            if k == 2: # 
                res[i,j] = res[i-1,j-1] 
    t = 0  
    for k in range(3):   
        if flag[k]:
            if k == 0: # s1 Link || s2 gap
                t += res[i-1,j] 
            if k == 1: # s2 Link || s1 gap
                t += res[i,j-1]
            if k == 2: # 匹配或突变
                t += res[i-1,j-1]
    while t > MOD: t -= MOD  ## it must be otherwise can make a different.
    res[i,j] = t
    return ret

seq = {}
temp = [list(range(len(s2)+1))] + [[n]* (len(s2)+1) for n in range(1,len(s1)+1)]
blast = np.array(temp) ## len(s1) : row | len(s2) :col
for i in range(1,len(s1) + 1):
    for j in range(1,len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            a = 0
        else:
            a = 1
        blast[i,j] = choose(blast[i-1,j]+1,blast[i,j-1]+1,blast[i-1,j-1]+a)

print(int(res[-1,-1])%MOD)