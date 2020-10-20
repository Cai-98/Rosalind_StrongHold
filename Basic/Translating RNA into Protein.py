RCT = open("D:/Userfiles/PTA/Rna_Codon_Table.txt",mode='r')
r_pro = {}
for line in RCT.readlines():
    line = line.strip('\n').split()
    for i in range(0,len(line),2):
        r_pro[line[i]] = line[i+1] if line[i+1] != 'Stop' else ' '
RCT.close()

rna = open("D:/Download/rosalind_prot.txt",mode='r')
out = open("D:/Download/output.txt",mode='w')
seq = rna.read().strip('\n')
for i in range(int(len(seq)/3)):
    key = seq[3*i:3*i+3]
    out.write(r_pro[key])
out.close()
rna.close()