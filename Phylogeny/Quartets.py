
res = []

def ran_get2(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            yield lst[i],lst[j]

with open("D:/Download/rosalind_qrt.txt",mode = 'r') as f:
    taxas = f.readline().strip('\n').split()
    for line in f.readlines():
        line = line.strip('\n')
        zeros = []
        ones = []
        for i in range(len(taxas)):
            if line[i] == 'x': continue
            elif line[i] == '1':ones.append(taxas[i])
            elif line[i] == '0':zeros.append(taxas[i])
        for a in ran_get2(ones):
            for b in ran_get2(zeros):
                if ((a,b) in res) or ((b,a) in res): continue
                res.append((a,b))
with open("D:/Download/output.txt",mode='w') as ff:
    for a,b in res:
        s = str(a) + ' ' + str(b) + '\n'
        s = s.replace('(','{').replace(')','}').replace("\'",'')
        ff.write(s)

        