
with open("D:/Download/rosalind_conv.txt",mode='r') as f:
    S1,S2 = list(map(lambda x: list(map(float,x.split())),f.read().strip().split('\n')))

D = {}
for i in S1:
    for j in S2:
        key = i-j;flag = 1
        for k in D.keys():
            if abs(k-key) <= 0.01: 
                D[k] += 1;flag = 0
                break
        if flag:
            D[key] = D.get(key,0) + 1

res = sorted(D.items(),key= lambda x:x[1],reverse=True)[0]
print(res[1],abs(res[0]),sep='\n')
#print(D)
