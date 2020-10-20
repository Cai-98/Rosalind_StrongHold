from math import factorial as fac
import numpy as np

N,m,g,k = map(int,input().split()) ## 一开始具有N个个体（不会增加）其中有m个显性基因，问经过g代之后有多大的概率大于k个隐形
num = 2*N ## the number of chromosome

## creating transition matrix
trans = np.zeros((num+1,num+1),dtype=float)
for i in range(num+1):
    for j in range(num+1):
        trans[j,i] = fac(num)/(fac(num-i)*fac(i)) * (j/num)**i * (1-j/num)**(num-i)
print(trans)
## initialize distribu vector
dis = np.zeros((1,num+1),dtype=float)
dis[0,num-m] = 1

for genr in range(g):
    dis = np.dot(dis,trans)
    print(*dis)
res = sum(dis[0,k:])

print(res)
