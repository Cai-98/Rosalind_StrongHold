import numpy as np
import time
tt = time.time()
seq = {}
with open("D:/Download/rosalind_smgb.txt",mode='r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if '>' in line :
            t = line 
            seq[t] = ''
        else:
            seq[t] += line 
s1,s2 = seq.values()
flag = 0
if len(s1) < len(s2): 
    s1,s2 = s2,s1
    flag = 1
pointer = np.zeros((len(s1)+1,len(s2)+1))
pointer[0,:] = [2] * (len(s2) + 1)
pointer[:,0] = [1] * (len(s1) + 1)
print("Read input file finished.Use %s"%(time.time()-tt))
def choose(a,b,c):
    res = max(a,b,c)
    #global gap
    if a == res: # s1 gap
        pointer[i,j] = 1
        #r1[(i,j)] = r1.get((i-1,j),'') + s1[i-1]
        #r2[(i,j)] = r2.get((i-1,j),'') + '-'
    elif b == res: # s2 gap
        pointer[i,j] = 2
        #r1[(i,j)] = r1.get((i,j-1),'') + '-'
        #r2[(i,j)] = r2.get((i,j-1),'') + s2[j-1]
    elif c == res: # 匹配或突变
        pointer[i,j] = 3
        #r1[(i,j)] = r1.get((i-1,j-1),'') + s1[i-1]
        #r2[(i,j)] = r2.get((i-1,j-1),'') + s2[j-1]
    return res

blast = np.zeros((len(s1)+1,len(s2)+1),dtype=float)
#blast[0,:] = list(range(0,-len(s2)-1,-1))
#blast[:,0] = list(range(0,-len(s1)-1,-1))
for i in range(1,len(s1) + 1):
    if i % 1000 == 0:print("read{}lines.Use {}".format(i,time.time()-tt))
    for j in range(1,len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            a = 1
        else:
            a = -1
        blast[i,j] = choose(blast[i-1,j]-1,blast[i,j-1]-1,blast[i-1,j-1]+a)

#print(r1)
#print(r2)
t = list(blast[:,-1])
r1 = ''; r2 = ''
score = max(t)
ind = t.index(score)
while True:
    if i > ind:
        r1 += s1[i-1]
        r2 += '-'
        i -= 1
    elif pointer[i,j] == 1:
        r1 += s1[i-1]
        r2 += '-'
        i -= 1
    elif pointer[i,j] == 2:
        r1 += '-'
        r2 += s2[j-1]
        j -= 1
    elif pointer[i,j] == 3:
        r1 += s1[i-1]
        r2 += s2[j-1]
        j -= 1 ; i -= 1
    if (j==0) and (i==0): break

if flag: r1,r2 = r2,r1
with open("D:/Download/output.txt",mode='w') as f:
    f.write(str(int(score)) + '\n')
    f.write(r1[::-1]+'\n')
    f.write(r2[::-1])