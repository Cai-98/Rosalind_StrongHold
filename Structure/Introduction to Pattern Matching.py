from itertools import permutations
seqs = open('D:/Download/rosalind_trie.txt').read().strip().split('\n')
OUT = open("D:/Download/out.txt",mode='w')
nodes = [''] + list( set( [ seq[:i] for seq in seqs for i in range(1,len(seq)+1)] ) )
for node1, node2 in permutations(nodes,2):
    if node2[:-1] == node1:
        OUT.write("%d %d %c"%(nodes.index(node1)+1, nodes.index(node2)+1, node2[-1])+'\n')