
with open("Monosiotopic mass table.txt",mode='r') as f:
    D = {}
    for line in f.readlines():
        line = line.strip('\n').split()
        D[float(line[1])] = line[0]

mass = [float(i.strip('\n')) for i in open("D:/Download/rosalind_spec.txt",mode='r').readlines()]
mass.sort()
res = ''
for i in range(1,len(mass)):
    demass = mass[i] - mass[i-1]
    for k in D.keys():
        if abs(k-demass) <= 0.01:break
    res += D[k]
print(res)