with open("D:/Download/rosalind_asmq.txt",mode='r') as f:
    contigs = f.read().strip().split('\n')
def NXX(sizes, x):
    return max([ L for L in sizes if sum([ ctg_len for ctg_len in sizes if ctg_len >= L ]) >= sum(sizes) * x ])
sizes = [len(c) for c in contigs]
print (NXX(sizes, 0.5), NXX(sizes, 0.75))