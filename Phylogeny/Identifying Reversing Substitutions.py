from Bio import Phylo
from io import StringIO
import time

NT = lambda : time.time()
st = NT()
with open("D:/Download/rosalind_rsub.txt",mode='r') as f:
    seq = {}
    tree_text = f.readline()[:-1]
    for line in f.readlines():
        line = line.strip('\n')
        if '>' in line:
            s = line[1:]
            seq[s] = ''
        else:
            seq[s] += line
print("Read Input file. Use %s sec."%(NT()-st))

tree = Phylo.read(StringIO(tree_text),format='newick') 
terminal = tree.get_terminals(order = 'postorder')
internal = tree.get_nonterminals(order = 'postorder')[:-1]
root = tree.get_nonterminals(order = 'postorder')[-1]
all_clade = terminal + internal + [root]
n = len(list(seq.values())[0]) # the length of sequence.

def get_child(clade):
    res = []
    for i in all_clade:
        if clade.is_parent_of(i) :
            res.append(i)
    return res

def get_parent(clade):
    t = [root] + tree.get_path(clade)
    return t[-2]

res = []
for clade in internal:
    print("Read {}. Use %s sec.".format(clade.name,(NT()-st)))
    parent = get_parent(clade)
    chidren = get_child(clade)
    a = seq[parent.name]
    c = seq[clade.name]
    for chi in chidren:
        b = seq[chi.name]
        path = clade.get_path(chi)
        if len(path) == 1:
            for i in range(n):
                if (a[i] == b[i]) and (c[i] != a[i]):
                    s = clade.name + ' ' + chi.name + ' ' + str(i+1) + ' ' +'->'.join([a[i],c[i],a[i]]) + '\n'
                    res.append(s)
        else:
            for i in range(n):
                flag = 1
                for chi2 in path[:-1]:
                    d = seq[chi2.name]
                    if d[i] != c[i]:
                        flag = 0 ; break
                if flag and (a[i] == b[i]) and (c[i] != a[i]):
                    s = clade.name + ' ' + chi.name + ' ' + str(i+1) + ' ' +'->'.join([a[i],c[i],a[i]]) + '\n'
                    res.append(s)

                


print("Write output file. Use %s sec."%(NT()-st))
with open("D:/Download/output.txt",mode='w') as f:
    for t in res:
        f.write(t)