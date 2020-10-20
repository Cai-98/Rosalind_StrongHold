def order(s):
    ret = []
    for i in s:
        ret.append(char.index(i))
    return tuple(ret)

import random
char = input().split()
n = int(input())
res = []
for i in range(1,n+1): ## 重复的字符数量
    temp = set()
    while len(temp) < len(char)**i:
        s = ''
        while len(s) < i:
            k = random.randint(0,len(char)-1)
            s += char[k]
        temp.add(s)
    res += list(temp)
res.sort(key = order)
res_out = [str(i) for i in res]
OUT = open("D:/Download/output.txt",mode='w')
OUT.write('\n'.join(res_out))
OUT.close()