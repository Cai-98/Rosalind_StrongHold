def find(s):
    i = 0
    flag = 0
    ps = []
    pss = ''
    while i < len(s)-3:
        key = s[i:i+3]
        if key == 'ATG':
            flag = 1
        if flag:
            if key in stop:
                ps.append(pss)
                flag = 0
                pss = ''
        if flag: pss += Dna_pro[key]
        i += 3
    return ps

def find_plus(s):
    out = []
    for i in range(3):
        t = find(s[i:])
        for j in t:
            index = []
            for x in range(len(j)):
                if j[x] == 'M':
                    index.append(x)
            for y in index:
                out.append(j[y:])
    return out

def rev_chain(s):
    a = ''
    s = ''.join(list(reversed(s)))
    D = {'A':'T','C':'G','G':'C','T':'A'}
    for i in s:
        a += D[i]
    return a

##DNA编码表的读取
Dtable = open("Dna_Codon_Table.txt",mode='r')
Dna_pro = {}
for line in Dtable.readlines():
    line = line.strip('\n').split()
    for i in range(0,len(line),2):
        Dna_pro[line[i]] = line[i+1]    
Dtable.close()

start = 'ATG' #起始密码子
stop_temp = filter(lambda x: x[1] == 'Stop',Dna_pro.items())
stop = [x for x,y in stop_temp]

seq = open("D:/Download/rosalind_orf.txt",mode='r')
out = open("D:/Download/output.txt",mode='w')
for line in seq.readlines():
    line = line.strip('\n')
    if '>' in line:
        s = ''
    else:
        s += line
st = rev_chain(s)
oa = find_plus(s)
ot = find_plus(st)
o = set(oa) | set(ot)
for i in list(o):
    if i =='':
        continue
    out.write(str(i)+'\n')
out.close()