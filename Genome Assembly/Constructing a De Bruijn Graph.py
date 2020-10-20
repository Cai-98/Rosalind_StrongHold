from Bio.Seq import reverse_complement as rc
with open("D:/Download/rosalind_dbru.txt",mode='r') as f:
    kmer = f.read().split('\n')

R = set()
for i in kmer:
    if not i: continue
    R.add((i[0:-1],i[1:]))
    t = rc(i)
    R.add((t[0:-1],t[1:]))


with open("D:/Download/out.txt",mode='w') as f:
    for i in sorted(list(R)):
        f.write('({}, {})\n'.format(i[0],i[1]))