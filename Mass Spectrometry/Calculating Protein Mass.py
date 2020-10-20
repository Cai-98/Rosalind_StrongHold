AA_mass = open("AA_Mass_Table.txt",mode='r')
AA = {}
for line in AA_mass.readlines():
    line = line.strip('\n').split()
    AA[line[0]] = float(line[1])
AA_mass.close()

seq = open("D:/Download/rosalind_prtm.txt",mode='r')
out = open("D:/Download/output.txt",mode='w')
s = ''
for line in seq.readlines():
    line = line.strip('\n')
    s += line
sum_p = 0
for i in s:
    sum_p += AA[i]
out.write(str(sum_p))
out.close()
seq.close()

