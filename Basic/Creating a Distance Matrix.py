## IN
with open("D:/Download/rosalind_pdst.txt",mode='r') as In :
    seq = {}
    t = -1
    for line in In.readlines():
        line = line.strip('\n')
        if '>' in line:
            t += 1
            seq[t] = ''
        else:
            seq[t] += line

def dist(s1,s2):
    out = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            out += 1
    return out/len(s1)
res = []
for i in range(len(seq)):
    tres = []
    for j in range(len(seq)):
        tres.append('{:.5f}'.format(dist(seq[i],seq[j])))
    res.append(tres)

with open("D:/Download/output.txt",mode='w') as output:
    for i in res:
        output.write(' '.join(i) + '\n')

