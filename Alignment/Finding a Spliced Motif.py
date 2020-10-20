Seq = open("D:/Download/rosalind_sseq.txt",mode='r')
re = []
s = ''
for line in Seq.readlines():
    line = line.strip('\n')
    if '>' in line :
        re.append(s)
        s = ''
    else:
        s += line
re.append(s)
A = list(re[1])
B = re[2]
res = []
j = 0
for i in range(len(B)):
    while A[j] != B[i]:
        j += 1
    res.append(j+1)
    j += 1
Seq.close()
out = open("D:/Download/output.txt",mode='w')
res = [str(i) for i in res]
out.write(' '.join(res))
out.close()