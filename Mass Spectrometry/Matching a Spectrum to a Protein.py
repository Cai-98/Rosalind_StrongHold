from multiprocessing import Pool
from time import time
st = time()
with open("Monosiotopic mass table.txt",mode='r') as f:
    D = {}
    for line in f.readlines():
        line = line.strip().split()
        D[line[0]] = float(line[1])

with open("D:/Download/rosalind_prsm.txt",mode='r') as f:
    num = int(f.readline().strip())
    print("There are %s protein to analyse."%num)
    protein = []
    for _ in range(num):
        protein.append(f.readline().strip())
    R = [float(i) for i in f.read().strip().split('\n')]

def complet_spectrum(s):
    ret = []
    def cal(s):
        ret = 0.0 
        for i in s:
            ret += D[i]
        return ret
        
    for i in range(len(s)):
        s1 = s[i:]
        s2 = s[:i]
        ret.append(cal(s1))
        ret.append(cal(s2))
    return ret

def m(pro):
    cs = complet_spectrum(pro)
    res = {}
    for i in R:
        for j in cs:
            key = i-j;flag=1
            for k in res.keys():
                if abs(k-key)<= 0.01:
                    res[k] += 1
                    flag = 0
                    break
            if flag:
                res[key] = 1
    print("FINISHED",time()-st,pro)
    return (pro,sorted(res.items(),key=lambda x: x[1],reverse=True)[0][1])

if __name__ == "__main__":
    with Pool(4) as p:
        r = p.map(m,protein)
    #print(r)
    temp = sorted(r,key = lambda x: x[1],reverse=True)
    print(*temp[0])
    #print(*temp[1])