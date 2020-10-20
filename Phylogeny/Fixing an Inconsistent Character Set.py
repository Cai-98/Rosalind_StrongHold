import numpy as np

with open("D:/Download/rosalind_cset.txt",mode='r') as f:
    #taxas = f.readline().strip('\n').split()
    Table = []
    for line in f.readlines():
        line = line.strip('\n')
        Table.append(list(line))
taxas = list(range(len(Table[0])))
chatable = np.array(Table,dtype=int)
del line, Table
reduce = True
ctable = np.copy(chatable)
link = []
while reduce:
    reduce = False
    i = -1
    while True:
        i += 1
        if i >= chatable.shape[0]: break
        row = chatable[i,:]
        for swich in [0,1]:
            finding = np.where(row == swich)[0]
            if len(finding) == 2: ## 一定是只有两个吗？
                i1 = finding[0]
                i2 = finding[1]
                if isinstance(taxas[i1],int) and isinstance(taxas[i2],int):
                    link.append((i1,i2))
                taxas[i1] = "({},{})".format(taxas[i1],taxas[i2])
                taxas = taxas[:i2] + taxas[i2+1:]
                chatable = np.delete(chatable,i,0)
                chatable = np.delete(chatable,i2,1)
                reduce = True
                break

print(link)
D = {}
for a,b in link:
    for i in range(ctable.shape[0]):
        if ctable[i,a] != ctable[i,b]:
            #print(i)
            D[i] = D.get(i,0) + 1
i,j = sorted(D.items(),key = lambda x:x[1])[-1]
with open("D:/Download/out.txt",mode='w') as f:
    new = np.delete(ctable,i,0)
    for i in range(new.shape[0]):
        s = ''.join(map(str,new[i,:])) + '\n'
        f.write(s)
