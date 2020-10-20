Codon = open("Rna_Codon_Table.txt",mode='r')
pro = {}
for line in Codon.readlines():
    line = line.strip('\n').split()
    for i in range(1,len(line),2):
        pro[line[i]] = pro.get(line[i],0) + 1
Codon.close()
pro['*'] = pro['Stop']
Pseq = open("D:/Download/rosalind_mrna.txt",mode='r')
seq = Pseq.read().replace('\n','')+'*'
times = 1
for i in seq:
    times *= pro[i]
    if times > 1000000:
        times %= 1000000
print(times)
Pseq.close()

