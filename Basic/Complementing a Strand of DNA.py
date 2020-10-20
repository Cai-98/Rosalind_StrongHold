DNA = open("D:/Download/rosalind_revc.txt",mode="r")
DNAs = open("D:/Download/output.txt",mode="w")
s = DNA.read()
ss = ''
for i in s:
    if i == "A":
        ss += "T"
    elif i == "C":
        ss += "G"
    elif i == "T":
        ss += "A"
    elif i == "G":
        ss += "C"
ls = list(ss)
ls.reverse()
DNAs.write(''.join(ls))
DNA.close()
DNAs.close()