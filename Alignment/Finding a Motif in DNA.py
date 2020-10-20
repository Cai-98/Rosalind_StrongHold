Seq = open("D:/Download/rosalind_subs.txt",mode='r')
out = open("D:/Download/output.txt",mode='w')
s , t,xx = Seq.read().split('\n')
i = 0
res = []
l = len(t)
while t in s[i:]:
    if s[i:i+l] == t:
        res.append(i+1)
    i += 1
c = ' '.join(list(map(str,res)))
out.write(c)
out.close()
Seq.close()