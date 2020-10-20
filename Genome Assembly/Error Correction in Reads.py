from Bio import Seq,SeqUtils
def Ham(s1,s2):
    a = 0
    b = 0
    s3 = Seq.reverse_complement(s1)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            a += 1
        if s3[i] != s2[i]:
            b += 1
    return min(a,b)

IN = open("D:/Download/rosalind_corr.txt",mode='r')
s = {}
for line in IN.readlines():
    line = line.strip('\n')
    if '>' in line :
        t = line
        s[t] = ''
    else:
        s[t] += line
IN.close()
cor = []
unk = []
seq = list(s.values())
for i in range(len(seq)):
    if Seq.reverse_complement(seq[i]) in seq:
        cor.append(seq[i])
    elif seq[i] in seq[i+1:]:
        cor.append(seq[i])
    else:
        unk.append(seq[i])
res = []
for wro in unk:
    for i in cor:
        if Ham(i,wro) == 1:
            res.append((wro,i))
            break



OUT = open("D:/Download/output.txt",mode='w')
for j in res:
    OUT.write('->'.join(j)+'\n')
OUT.close()