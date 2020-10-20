
with open("D:/Download/rosalind_eval.txt",mode='r') as f:
    n,s,A = f.read().strip().split('\n')
n = int(n); A = [float(i) for i in A.split()]
res = []

for gc in A:
    pgc = gc/2
    pat = (1-gc)/2
    ps = 1
    for i in range(len(s)):
        if s[i] in ('G','C'): ps *= pgc
        elif s[i] in ('A','T'): ps *= pat
    res.append(ps*(n-len(s)+1))
print(*res)