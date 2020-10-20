import math 
IN = open("D:/Download/rosalind_prob.txt",mode='r')
seq  = IN.readline().strip('\n')
GC = list(map(float,IN.readline().split()))
AT = [(1-i) for i in GC]
B = []
for i in range(len(GC)):
    res = 0
    for j in seq:
        if (j == 'C') or (j == 'G'):
            res += math.log10(GC[i]/2)
        else:
            res += math.log10(AT[i]/2)
    B.append(res)
print(*B)
IN.close()