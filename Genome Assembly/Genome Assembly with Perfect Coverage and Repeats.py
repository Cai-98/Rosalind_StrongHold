
with open("D:/Download/rosalind_grep.txt",mode='r') as f:
    reads = f.read().strip().split('\n')

k = len(reads[0])
edge = lambda x: (x[0:k-1],x[1:k+1])
Edge = [edge(i) for i in reads[1:]]

def cover(s,edges):
    '''
    plus = []
    for index,item in enumerate(edges):
        l = len(item[0])
        if item[0] == s[-l:]:
            plus.append(index)
    '''
    plus = [index for index,item in enumerate(edges) if item[0]==s[1-k:]]
    if len(plus) == 0:
        return s if edges == [] else []
    else:
        return [cover(s+edges[i][1][-1],edges[:i]+edges[i+1:]) for i in plus]

def flat(lst):
    res = []
    for i in lst:
        if isinstance(i,list):
            res += flat(i)
        else:
            res.append(i)
    return res

cirular = [cir[:len(reads)] for cir in set(flat(cover(reads[0],Edge)))]

print('\n'.join(cirular))