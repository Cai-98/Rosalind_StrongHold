#read in
Fasta = open("D:/Download/rosalind_cons.txt",mode='r')
out = open("D:/Download/output.txt",mode='w')
Seq = [""]
i = 0
for line in Fasta.readlines():
    line = line.strip('\n')
    if '>' in line:
        i += 1
        Seq.append("")
    else:
        Seq[i] += line
Fasta.close()
Seq = Seq[1:]
#deal with 
prf = {"A":[],"C":[],"G":[],"T":[]}
con = []
l = len(Seq[0])
for i in range(l):
    scount = {"A":0,"C":0,"G":0,"T":0}
    for s in Seq:
        if s[i] == 'A':
            scount['A'] += 1
        elif s[i] == 'C':
            scount['C'] += 1
        elif s[i] == 'G':
            scount['G'] += 1
        elif s[i] == 'T':
            scount['T'] += 1
    prf["A"].append(str(scount['A']))
    prf["C"].append(str(scount['C']))
    prf["G"].append(str(scount['G']))
    prf["T"].append(str(scount['T']))
    sortS = sorted(scount.items(),key=lambda x: x[1],reverse = True) 
    con.append(sortS[0][0])
# write
conseq = ''.join(con)
a = "A: "+ ' '.join(prf["A"])
c = "C: "+ ' '.join(prf["C"])
g = "G: "+ ' '.join(prf["G"])
t = "T: "+ ' '.join(prf["T"])
out.write('\n'.join([conseq,a,c,g,t]))
out.close()
