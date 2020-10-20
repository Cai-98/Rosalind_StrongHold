from math import sqrt
from copy import deepcopy
Lt = [int(i) for i in open("D:/Download/rosalind_pdpl.txt",mode='r').readline().strip().split()]
len_x = int((1+sqrt(1+8*len(Lt)))/2)
Lt.sort()
lmax = Lt[-1]
SL = set(Lt)
SL.add(0)

def cal(i):
    temp = [0];flag = 1
    L = deepcopy(Lt)
    while True:
        t = sum(temp)+L[i]
        if (t in SL) and ((lmax-t) in SL) and ((L[i]+temp[-1]) in SL):
            temp.append(L[i]);L.remove(L[i]);i=0;continue
        i += 1
        if (len(temp) == 2) and flag:
            rem = i
            flag = 0
        if (sum(temp) > lmax) or (i >= len(L)):
            print("Fail")
            return cal(rem)
        
        if (sum(temp) == lmax) and (len(temp) == len_x):
            print("Success")
            #print(*temp)
            return temp

sep = cal(0)
res = []
for i in range(len(sep)):
    res.append(sum(sep[:i+1]))
print(*res)