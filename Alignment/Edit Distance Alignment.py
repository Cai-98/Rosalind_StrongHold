import numpy as np

seq = {}
with open("D:/Download/rosalind_edta.txt",mode='r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if '>' in line :
            t = line 
            seq[t] = ''
        else:
            seq[t] += line 
s1,s2 = seq.values()
r1,r2 = [{},{}]

def choose(a,b,c):
    res = min(a,b,c)
    if a == res: # s1 gap
        r1[(i,j)] = r1.get((i-1,j),'') + s1[i-1]
        r2[(i,j)] = r2.get((i-1,j),'') + '-'
    elif b == res: # s2 gap
        r1[(i,j)] = r1.get((i,j-1),'') + '-'
        r2[(i,j)] = r2.get((i,j-1),'') + s2[j-1]
    elif c == res: # 匹配或突变
        r1[(i,j)] = r1.get((i-1,j-1),'') + s1[i-1]
        r2[(i,j)] = r2.get((i-1,j-1),'') + s2[j-1]
    return res

temp = [list(range(len(s2)+1))] + [[n]* (len(s2)+1) for n in range(1,len(s1)+1)]
blast = np.array(temp) ## len(s1) : row | len(s2) :col
for i in range(1,len(s1) + 1):
    for j in range(1,len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            a = 0
        else:
            a = 1
        blast[i,j] = choose(blast[i-1,j]+1,blast[i,j-1]+1,blast[i-1,j-1]+a)

#print(r1)
#print(r2)

with open("D:/Download/output.txt",mode='w') as f:
    f.write(str(blast[-1,-1]) + '\n')
    f.write(r1[(len(s1),len(s2))]+'\n')
    f.write(r2[(len(s1),len(s2))])