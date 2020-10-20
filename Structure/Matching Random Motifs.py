n,x = map(eval,input().split())
seq = input()
gc = x/2
at = (1-x)/2
D = {'A':at,'T':at,'G':gc,'C':gc}
p = 1
for i in range(len(seq)):
    p *= D[seq[i]]  ## 得到相同序列的概率

## 已知事件发生的概率p 重复n次 至少有一次发生的概率是多少
res = 1 - (1-p)**n
#for i in range(1,n+1):
#    res += (1-p)**(n-i) * p **i
print('{:.3f}'.format(res))