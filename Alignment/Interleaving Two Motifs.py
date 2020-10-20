from Bio.pairwise2 import align as al

with open("D:/Download/rosalind_scsp.txt") as f:
    s1 = f.readline().strip()
    s2 = f.readline().strip()
align = al.globalms(s1,s2,1,0,0,0)[0]
r1 = align.seqA
r2 = align.seqB
result = ''
for i in range(len(r1)):
    if r1[i] == '-':result += r2[i]
    elif r2[i] == '-':result += r1[i]
    else:result += r1[i]
print(result)