from Bio import Phylo
from io import StringIO

with open("D:/Download/rosalind_nkew.txt",mode='r') as f:
    cases = f.read().split('\n\n')

for case in cases:
    tree_text , taget = case.split(';\n')
    x,y = taget.split()
    tree = Phylo.read(StringIO(tree_text),'newick')
    print(int(tree.distance(x,y)),end = ' ')