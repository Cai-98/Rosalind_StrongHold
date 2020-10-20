import copy
Seq = open("D:/Download/rosalind_lgis.txt", mode='r')
n = int(Seq.readline().strip('\n'))
seq = []
for line in Seq.readlines():
    line = line.strip('\n').split()
    line = [int(i) for i in line]
    seq.extend(line)
Seq.close()
## increasing len finding
flag = [1] * len(seq)
insseq = [[i] for i in seq]
for i in range(len(seq)):
    for j in range(i):
        if (seq[i] >= seq[j]) and (flag[i] < flag[j] + 1):
            flag[i] = flag[j] + 1
            insseq[i] = [seq[i]] + insseq[j]
res_ins = insseq[flag.index(max(flag))]
res_ins.reverse()

## decreasing len finding
flag = [1] * len(seq)
desseq = [[i] for i in seq]
for i in range(len(seq)):
    for j in range(i):
        if (seq[i] <= seq[j]) and (flag[i] < flag[j] + 1):
            flag[i] = flag[j] + 1
            desseq[i] = [seq[i]] + desseq[j]
res_des = desseq[flag.index(max(flag))]
res_des.reverse()

out = open("D:/Download/output.txt",mode='w')
write = lambda x: ' '.join(list(map(str,x)))
out.write(write(res_ins) + '\n')
out.write(write(res_des))
out.close()