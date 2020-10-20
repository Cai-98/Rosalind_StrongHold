from time import time as ti

st = ti()
class Node():
    def __init__(self,name,lable,child=[],depth=0):
        self.name = name
        self.child = list(child)
        self.depth = depth
        self.lable = lable

    def isterminal(self):
        if self.child == []:return True
        else:return False 

    def acum_depth(self):
        if self.isterminal():
            return 1
        else:
            ret = self.depth
            for i in self.child:
                ret += i.acum_depth()
            self.depth = ret
            return ret

nodecl = {}
with open("D:/Download/rosalind_lrep.txt",mode='r') as f:
    seq = f.readline().strip()
    num = int(f.readline().strip())
    for line in f.readlines():
        par,chi,loc,leng = line.strip().split()
        loc,leng = map(int,(loc,leng))
        if (par == 'node1') and ('node1' not in nodecl.keys()):
            P = Node(name='',lable='node1')
            nodecl['node1'] = P
        else:
            P = nodecl[par]
        C = Node(name=P.name+seq[loc-1:loc-1+leng],lable=chi)
        nodecl[chi] = C
        P.child.append(C)
        #P.depth += 1
print("READ.%s"%(ti()-st))
nodecl['node1'].acum_depth()
m = 0
for n in nodecl.values():  
    if (n.depth >= num) and (len(n.name)>m):
        res = n
        m = len(res.name)

print(res.name)