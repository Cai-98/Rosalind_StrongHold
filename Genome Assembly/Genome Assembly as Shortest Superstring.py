def likly(seq): 
    maxlen = -1
    maxind = []
    res = ''
    for i in range(len(seq)):
        for j in range(len(seq)):
            if i == j : continue
            a , b = seq[i] , seq[j]
            t = 0
            while a[t:] not in b:
                t += 1
            if len(a)-t > maxlen:
                maxlen = len(a) - t
                maxind = [i,j]
                res = a[:t] + b
    re = [seq[s] for s in range(len(seq)) if s not in maxind] + [res]
    return re

## Reading
Seq = open("D:/Download/rosalind_long.txt",mode='r')
seq = []
s = ''
for line in Seq.readlines():
    line = line.strip('\n')
    if '>' in line:
        seq.append(s)
        s = ''
    else:
        s += line
seq.append(s)
seq = seq[1:]

## rank
while len(seq) != 1:
    seq = likly(seq)

## out
out = open("D:/Download/output.txt",mode='w')
out.write(seq[0])
out.close()