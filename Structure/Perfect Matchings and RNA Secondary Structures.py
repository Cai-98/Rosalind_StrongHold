Seq = open("D:/Download/rosalind_pmch.txt",mode='r')
head = Seq.readline()
s = ''
for line in Seq.readlines():
    s += line.strip('\n')
Seq.close()
def fac(i):
    s = 1
    for j in range(1,i+1):
        s *= j
    return s

AU = 0
CG = 0
for n in s :
    if n == 'A':
        AU += 1
    elif n == 'C':
        CG += 1
print(fac(AU)*fac(CG))