from Bio import Phylo
from io import StringIO
f = open('D:/Download/rosalind_nwck.txt',mode='r')
seq = f.read().split('\n\n')

dis = []
for s in seq:
    if s =='':continue
    a,b = s.split(';\n')
    x,y = b.split()
    tree = Phylo.read(StringIO(a),format='newick')
    mrca = tree.common_ancestor(x, y)
    #print(mrca)
    d =  len(mrca.get_path(x)) + len(mrca.get_path(y))
    dis.append(d)
print(' '.join(map(str,dis)))