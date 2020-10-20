with open("Monosiotopic mass table.txt",mode='r') as f:
    Mass = {}
    for line in f.readlines():
        line = line.strip().split()
        Mass[float(line[1])] = line[0]

with open("D:/Download/rosalind_sgra.txt",mode='r') as f:
    L = [float(i) for i in f.read().strip().split('\n')]
L.sort(reverse=True)
Dire = {}
def judge(a,b):
    if len(a)>=len(b):
        return a
    else:
        return b

for i in range(len(L)):
    for j in range(len(L)):
        if i == j:continue
        value = abs(L[i]-L[j])
        for key in Mass.keys():
            if abs(value - key) <= 0.01:
                v,k = sorted([L[i],L[j]])
                Dire[v] = judge(Dire.get(k,'') + Mass[key],Dire.get(v,''))
res = sorted(Dire.items(),key = lambda x:len(x[1]),reverse=True)[0][1]
print(res[::-1])
#print(Dire)