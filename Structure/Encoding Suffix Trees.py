from itertools import permutations
from collections import defaultdict
from time import time as now

st = now()
seq = open("D:/Download/rosalind_suff.txt",mode='r').readline().strip()
suffix = []
for i in range(1,len(seq)+1):
    suf = seq[-i:]
    suffix.append(suf)
print("READ INPUT FILE. USE %s"%(now()-st))
name = {} ; dire = {}
class Trie:
    available = 1
    def __init__(self):
        self.label = str(Trie.available)
        self.child_nodes = defaultdict(Trie)
        Trie.available += 1

    def add_child(self, child):
        if not child: return
        self.child_nodes[child[0]].add_child(child[1:])

    def get_trie(self):
        global name,dire
        for char,child in self.child_nodes.items():
            a,b,c = (self.label,child.label,char)
            dire[a] = dire.get(a,[]) + [b]
            name[b] = c
            child.get_trie()

T = Trie()
for s in suffix:
  T.add_child(s)
T.get_trie()
  
print("BUILD DIC. USE %s"%(now()-st))

name[1] = ''
def get_name(node,par = ''):
    if node not in dire.keys():
        return par+name[node],-1
    elif len(dire[node]) == 1:
        return get_name(dire[node][0],par=par+name[node])
    else:
        return par+name[node],node

def get_realname(node):
    res = []
    for i in dire[node]:
        temp = get_name(i)
        if temp[1]==-1:
            res.append(temp[0])
        else:
            res.append(temp[0])
            res += get_realname(temp[1])
    #print("CAL NODE%s. USE %s"%(node,now()-st))
    return res


with open("D:/Download/out.txt",mode='w') as f:
    f.write('\n'.join(get_realname("1")))