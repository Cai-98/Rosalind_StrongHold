def judge(a,b):
    if a > b:
        a , b = b , a 
    if (a == 'A') and (b == 'G'):
        return 1
    elif (a == 'C') and (b == 'T'):
        return 1
    else:
        return 0

Seq = open("D:/Download/rosalind_tran.txt",mode='r')
s = {}
for line in Seq.readlines():
    line = line.strip('\n')
    if '>' in line:
        t = line
        s[t] = ''
    else:
        s[t] += line
A , B = s.values()
s1 = 0
s2 = 0
for i in range(len(A)):
    if A[i] == B[i]:
        continue
    elif judge(A[i],B[i]):
        s1 += 1
    else:
        s2 += 1
Seq.close()
print(s1/s2)