def rev_chain(s):
    a = ''
    s = ''.join(list(reversed(s)))
    D = {'A':'T','C':'G','G':'C','T':'A'}
    for i in s:
        a += D[i]
    return a

def t2s(t):
    a = list(map(str,t))
    return ' '.join(a)

Seq = open("D:/Download/rosalind_revp.txt",mode='r')
s = ''
for line in Seq.readlines():
    line = line.strip('\n')
    if '>' in line :
        continue
    else:
        s += line
Seq.close()
res = []
out = open("D:/Download/output.txt",mode='w')
for i in range(len(s)):
    for j in range(4,13):
        if i + j > len(s):
            break
        if s[i:i+j] == rev_chain(s[i:i+j]):
            res.append((i+1,j))
for t in res:
    out.write(t2s(t)+'\n')
out.close()
