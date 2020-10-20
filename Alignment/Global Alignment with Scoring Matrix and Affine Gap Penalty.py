import numpy as np

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

seq = {}
with open("D:/Download/rosalind_gaff.txt",mode='r') as f:
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
    res = max(a,b,c)
    if a == res: # s1 gap
        r1[(i,j)] = r1.get((rw,j),'') + s1[int(rw):int(i)]
        r2[(i,j)] = r2.get((rw,j),'') + '-'*int(i-rw)
    elif b == res: # s2 gap
        r1[(i,j)] = r1.get((i,cl),'') + '-'*int(j-cl)
        r2[(i,j)] = r2.get((i,cl),'') + s2[int(cl):int(j)]
    elif c == res: # 匹配或突变
        r1[(i,j)] = r1.get((i-1,j-1),'') + s1[i-1]
        r2[(i,j)] = r2.get((i-1,j-1),'') + s2[j-1]
    return res

def gapi(row,col):
    max = blast[row-1,col] - 11
    for k in range(0,row):
        score = blast[k,col] - 11 - (row - k - 1)
        if score > max:
            max = score
            global rw
            rw = k
    return max

def gapj(row,col):
    max = blast[row,col-1] - 11
    for k in range(0,col):
        score = blast[row,k] - 11 - (col - k - 1)
        if score > max:
            max = score
            global cl 
            cl = k
    return max

seq = {}
blast = np.zeros((len(s1)+1,len(s2)+1))
blast[0,:] = [0] + list(range(-11,-11-len(s2),-1))
blast[:,0] = [0] + list(range(-11,-11-len(s1),-1))
for i in range(1,len(s1) + 1):
    for j in range(1,len(s2) + 1):
        rw,cl = i-1,j-1
        blast[i,j] = choose(gapi(i,j),gapj(i,j),blast[i-1,j-1]+BLO[(s1[i-1],s2[j-1])])


with open("D:/Download/output.txt",mode='w') as f:
    f.write(str(int(blast[-1,-1])) + '\n')
    f.write(r1[(len(s1),len(s2))]+'\n')
    f.write(r2[(len(s1),len(s2))])