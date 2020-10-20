Seq = open("D:/Download/rosalind_grph.txt",mode='r')
seq = {}
for line in Seq.readlines():
    line = line.strip('\n')
    if '>' in line:
        sn = line[1:]
        seq[sn] = ''
    else:
        seq[sn] += line
Seq.close()
###
edge = []
for s1 in seq.keys():
    for s2 in seq.keys():
        if s1 == s2:
            continue
        if seq[s1][-3:] == seq[s2][:3]:
            edge.append((s1,s2))
out = open("D:/Download/output.txt",mode='w')
for i in edge:
    out.write(' '.join(i)+'\n')
out.close()