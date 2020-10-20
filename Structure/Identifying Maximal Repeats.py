s = open("D:/Download/rosalind_mrep.txt").readline().strip()
n=len(s)
S=set()
for a in range(n):
  for b in range(a+1,n):
    if a>0 and b>0 and s[a-1]==s[b-1]: continue
    k=0
    while b+k<n and s[a+k]==s[b+k]:
        k+=1
    if k>=20:
        S.add(s[a:a+k])
print(S)