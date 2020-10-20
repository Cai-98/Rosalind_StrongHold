Seq = open("D:/Download/rosalind_lcsm.txt",mode='r')
seq = {}
for line in Seq.readlines():
    line = line.strip('\n')
    if '>' in line:
        s = line[1:]
        seq[s] = ''
    else:
        seq[s] += line
Seq.close()
maxlen = 1
maxseq = ''
seql = list(seq.values())
i = 0
l = len(seql[0])
while i+maxlen < l:
    t = seql[0][i:i+maxlen+1]
    flag = 1
    for s in seql:
        if t not in s:
            flag = 0
            break
    if flag:
        maxlen += 1
        maxseq = t
    else:
        i += 1
out = open("D:/Download/output.txt",mode='w')
out.write(maxseq)
out.close()