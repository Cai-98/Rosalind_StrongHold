def sub(a,b):
    i = 0
    l = len(a)
    while a in b[i:]:
        i += 1
    return b[:i-1]+b[i+l-1:]

DCT = open("Dna_Codon_Table.txt",mode='r')
pro = {}
for line in DCT.readlines():
    line = line.strip('\n').split()
    for i in range(0,len(line),2):
        pro[line[i]] = line[i+1] if line[i+1] != 'Stop' else ' '
DCT.close()
out = open("D:/Download/output.txt",mode='w')
Seq = open("D:/Download/rosalind_splc.txt",mode='r')
flag = 1
seq = []
s = ''
for line in Seq.readlines():
    line = line.strip('\n')
    if '>' in line :
        seq.append(s)
        s = ''
    else:
        s += line
seq.append(s)
long_s = seq[1]
short_s = seq[2:]
for i in short_s:
    while i in long_s:
        long_s = sub(i,long_s)
for i in range(0,len(long_s),3):
    out.write(pro[long_s[i:i+3]])
out.close()




    