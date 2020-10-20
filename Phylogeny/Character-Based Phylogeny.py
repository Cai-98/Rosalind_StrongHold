import numpy as np

with open("D:/Download/rosalind_chbp.txt",mode='r') as f:
    taxas = f.readline().strip('\n').split()
    Table = []
    for line in f.readlines():
        line = line.strip('\n')
        Table.append(list(line))

chatable = np.array(Table,dtype=int)

reduce = True
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
                taxas[i1] = "({},{})".format(taxas[i1],taxas[i2])

                taxas = taxas[:i2] + taxas[i2+1:]
                chatable = np.delete(chatable,i,0)
                chatable = np.delete(chatable,i2,1)
                reduce = True
                break

with open("D:/Download/out.txt",mode='w') as f:
    f.write("(" + ",".join(taxas) + ");")
