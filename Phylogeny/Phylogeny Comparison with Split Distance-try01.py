from Bio import Phylo as phy
from io import StringIO as stio
import multiprocessing
import time
st = time.time()
with open("D:/Download/rosalind_sptd.txt",mode='r') as f:
    taxas = f.readline().strip('\n').split()
    tree_texta = f.readline().strip('\n')[:-1]
    tree_textb = f.readline().strip('\n')[:-1]

def splitree(tree):
    #print(tree)
    terminal = tree.get_terminals()
    internal = tree.get_nonterminals()
    n = len(internal) ; all_pos = int(n*(n-1)/2) ; count = 1
    ret = []
    res = set()
    for i in range(len(internal)):
        for j in range(i+1,len(internal)):
            print("dealing with {}/{}".format(count,all_pos)) ; count+=1
            clade0 = internal[i]
            clade1 = internal[j]
            route = len(clade0.get_path(clade1)) if clade0.get_path(clade1) else 99
            if route != 1: continue 
            for ter in terminal:
                if clade0 not in tree.trace(clade1,ter):
                    ret.append(taxas.index(ter.name))
            if len(ret) <= (len(taxas)//2):
                res.add(''.join(map(str,sorted(ret))))
            else:
                rett = [i for i in range(len(taxas)) if i not in ret]
                res.add(''.join(map(str,sorted(rett))))
    return res

if __name__ == "__main__":
    with multiprocessing.Pool(2) as p:
        treea = phy.read(stio(tree_texta),format='newick')
        treeb = phy.read(stio(tree_textb),format='newick')
        A,B = p.map(splitree,[treea,treeb])
    x = len(A&B)
    print("Used %s" %(time.time()-st))
    print(2*(len(taxas)-3)-2*x)