DNA = open("D:/Download/rosalind_rna.txt",mode="r")
RNA = open("D:/Download/output.txt",mode="w")
for line in DNA.readlines():
    line = line.replace("T","U")
    RNA.write(line)
DNA.close()
RNA.close()
