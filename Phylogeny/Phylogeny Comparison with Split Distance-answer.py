import sys
from Bio import Phylo
from io import StringIO

def charset(tree, taxa):
  cs = set()
  for anc in tree.get_nonterminals():
    u = ['0'] * len(taxa)
    for t in anc.get_terminals():
       u[taxa.index(t.name)] = '1'
    #if u[0] == '1':
       #u = [(['0','1'][x == '0']) for x in u]
    cs.add(''.join(u))
  return cs

f = open("D:/Download/rosalind_sptd.txt",mode='r')
taxa = f.readline().split()
t1 = Phylo.read(StringIO(f.readline()), 'newick')
t2 = Phylo.read(StringIO(f.readline()), 'newick')

cs1 = charset(t1, taxa)
cs2 = charset(t2, taxa)
print(len (cs1 ^ cs2))
f.close()