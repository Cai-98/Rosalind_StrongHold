IN = open("D:/Download/rosalind_kmer.txt",mode='r')
name = IN.readline()
s = ''
for line in IN.readlines():
    s += line.strip('\n')
IN.close()

mer = {}
for i in range(len(s)-4+1):
    mer[s[i:i+4]] = mer.get(s[i:i+4],0) + 1
out = sorted(mer.items(),key=lambda x: x[0])
out = [str(out[i][1]) for i in range(len(out))]
print(' '.join(out))