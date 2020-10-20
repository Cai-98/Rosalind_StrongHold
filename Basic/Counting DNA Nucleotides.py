DNA_list = open("D:/Userfiles/PTA/rosalind_dna.txt",mode="r")
DNA_count = open("output.txt",mode="w")
countnum = {"A":0,"G":0,"C":0,"T":0}
for line in DNA_list.readlines():
    line = line.strip("\n")
    for i in line:
        countnum[i] += 1
s = list(map(str,[countnum["A"],countnum["C"],countnum["G"],countnum["T"]]))
DNA_count.write(' '.join(s))
DNA_list.close()
DNA_count.close()