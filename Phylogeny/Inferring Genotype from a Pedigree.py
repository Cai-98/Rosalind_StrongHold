from Bio import Phylo as ph
from io import StringIO as sio
import numpy as np
from numpy import dot
with open("D:/Download/rosalind_mend.txt",mode='r') as f:
    tree = f.read().strip('\n')[:-1]
tree = ph.read(sio(tree),'newick')

D = {}
D[('AA','AA')] = [1,0,0]
D[('AA','Aa')] = [0.5,0.5,0]
D[('AA','aa')] = [0,1,0]
D[('Aa','aa')] = [0,0.5,0.5]
D[('Aa','Aa')] = [0.25,0.5,0.25]
D[('aa','aa')] = [0,0,1]
## AA Aa aa

A1 = np.array([D[('AA','AA')],D[('AA','Aa')],D[('AA','aa')]])
A0 = np.array([D[('AA','aa')],D[('Aa','aa')],D[('aa','aa')]])
A2 = np.array([D[('AA','Aa')],D[('Aa','Aa')],D[('Aa','aa')]])

inter = tree.get_nonterminals(order = 'postorder')
tree.root = inter[-1] ; tree.rooted = True
termi = tree.get_terminals()

def get_parent(clade):
    ret = []
    for i in termi+inter:
        if clade.is_parent_of(i) and len(tree.trace(clade,i)) == 2:
            ret.append(i)
    return ret

def cal(m1,m2):
    return(m2[0]*dot(m1,A1) + m2[1]*dot(m1,A2) + m2[2]*dot(m1,A0))

for clade in termi:
    if clade.name == 'AA':
        clade.comment = np.array([1,0,0])
    elif clade.name == 'Aa':
        clade.comment = np.array([0,1,0])
    elif clade.name == 'aa':
        clade.comment = np.array([0,0,1])

for clade in inter:
    par = get_parent(clade)
    for i in par: 
        if not len(i.comment) : 
            print(clade,par)
            print(i.comment)
            exit("ERRO")
    if len(par) != 2: 
        print(clade,par)
        exit("ERRO2")

    clade.comment = cal(par[1].comment,par[0].comment)

print(*tree.root.comment)