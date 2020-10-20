from Bio import Phylo
from io import StringIO
import time,copy

NT = lambda : time.time()
st = NT()
with open("D:/Download/rosalind_alph.txt",mode='r') as f:
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
internal = tree.get_nonterminals(order = 'postorder')
all_clade = terminal + internal
n = len(list(seq.values())[0]) # the length of sequence.

def get_child(clade):
    res = []
    for i in all_clade:
        if clade.get_path(i) and (len(clade.get_path(i)) == 1) :
            res.append(i)
    return res

def get_parent(clade):
    t = [internal[0]] + tree.get_path(clade)
    return t[-2]

def get_consence(clade):
    consence = []
    for _ in range(n): consence.append(dict())
    child = get_child(clade)
    pre = copy.deepcopy(consence)
    #if clade != internal[0]:
        #child.append(get_parent(clade))
    for i in range(n):## 对于每个位点而言
        for chi in child: ## 考虑每个子代的操作步数
            if chi in terminal:
                v = seq[chi.name] ## 子代的序列
                for chact in 'ATCG-':## 考虑每种可能的操作步数
                    if chact == v[i]:consence[i][chact] = consence[i].get(chact,0)
                    else:consence[i][chact] = consence[i].get(chact,0) + 1
                    pre[i][chact] = pre[i].get(chact,{})
                    pre[i][chact][chi.name] = seq[chi.name][i]
            else: # where the question is
                temp = clade_consence[chi.name][i]
                for chact in 'ACTG-':
                    #new_temp = {}
                    min = 999999                  
                    for k,v in temp.items():
                        if (k == chact) and (temp.get(k,0) <min):
                            min = temp.get(k,0);k_=k
                        elif (temp.get(k,0) + 1) < min:
                            min = temp.get(k,0) + 1;k_=k
                    consence[i][chact] = consence[i].get(chact,0) + min
                    pre[i][chact] = pre[i].get(chact,{})
                    pre[i][chact][chi.name] = k_
    return consence,pre

clade_consence = {}
clade_pre = {}
for clade in internal:
    clade_consence[clade.name],clade_pre[clade.name] = get_consence(clade)
print("construct tree and rember root. Use %s sec."%(NT()-st))

res = 0
resq = {}
for i in range(n):
    tempr = sorted(clade_consence[internal[-1].name][i].items(),key = lambda x:x[1],reverse = False)[0]
    res += tempr[1]
    def reconstruct(clade,chact):
        if clade in terminal:return None
        resq.setdefault(clade.name,'')
        resq[clade.name] += chact
        child = get_child(clade)
        for chi in child:
            reconstruct(chi,clade_pre[clade.name][i][chact][chi.name]) 
    reconstruct(internal[-1],tempr[0])
print("Reconstruct DNA seq of internal nodes. Use %s sec."%(NT()-st))

print(res)
OUT = open("D:/Download/output.txt",mode='w')
OUT.write(str(res)+'\n')
for k,v in resq.items():
    OUT.write('>'+k+'\n'+v+'\n')
OUT.close()