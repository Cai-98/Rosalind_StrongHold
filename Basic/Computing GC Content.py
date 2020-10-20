def coutGC(s):
    l = len(s)
    gc = 0
    for i in s:
        if (i == "G") or (i == "C"):
            gc += 1
    return gc/l

DNA = open("D:/Download/rosalind_gc.txt",mode="r")
#OUT = open("D:/Download/output.txt",mode="w")
GC = {}
for line in DNA.readlines():
    line = line.strip("\n")
    if ">" in line:
        s = line[1:]
    else:
        GC[s] = GC.get(s,"") + line

for key in GC.keys():
    GC[key] = coutGC(GC[key])
#print(list(GC.items()))
slist = sorted(GC.items(),key = lambda x:x[1],reverse=True)
print(slist[0][0])
print(slist[0][1]*100)

