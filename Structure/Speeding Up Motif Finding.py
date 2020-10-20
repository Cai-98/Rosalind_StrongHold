IN = open("D:/Download/rosalind_kmp.txt",mode='r')
seq = ''
name = IN.readline()
for line in IN.readlines():
    seq += line.strip('\n')
IN.close()

arra = [0] * len(seq)
'''
for i in range(1,len(seq)):
    t = 0
    s = seq[:i+1]
    for j in range(i,1,-1):
        if s[j] != s[0] : continue
        if s[j:i+1] == s[0:i+1-j]:
            t = i-j+1
    arra.append(t)
'''
j = 1
while j < len(seq):
    if seq[j] == seq[0]:
        t = 1
        arra[j] = max(t,arra[j])
        for i in range(j+1,len(seq)):
            if seq[i] == seq[i-j]:
                t += 1
            else:
                break
            arra[i] = max(t,arra[i])
    j += 1

OUT = open("D:/Download/output.txt",mode='w')
arra = [str(i) for i in arra]
OUT.write(' '.join(arra))
OUT.close()