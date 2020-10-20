from Bio import Phylo
from io import StringIO

x = open("D:/Download/rosalind_ctbl.txt",mode='r').read().strip(';\n')
tree = Phylo.read(StringIO(x),'newick')
clade_list = tree.get_nonterminals()
terminal = tree.get_terminals()
terminal.sort(key=lambda x: x.name)
res = []
for clade in clade_list:
    temp = []
    for ter in terminal:
        if clade.is_parent_of(ter):
            temp.append(1)
        else:
            temp.append(0)
    res.append(temp)

with open("D:/Download/output.txt",mode='w') as f:
    for i in range(1,len(res)):
        s = ''.join(map(str,res[i])) + '\n'
        f.write(s)