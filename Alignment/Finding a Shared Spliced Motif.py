### INPUT
IN = open("D:/Download/rosalind_lcsq.txt",mode='r')
seq = {}
for line in IN.readlines():
    line = line.strip('\n')
    if '>' in line:
        t = line
        seq[t] = ''
    else:
        seq[t] += line
IN.close()
s1 , s2 = seq.values()

## Dynamic Programming
flag = [''] * (len(s2) + 1)
for i in range(len(s1)):
    flag_ = list(flag)
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            flag[j+1] = flag_[j] + s2[j] ## 必须是flag_ 否则会导致重复添加
        else:
            flag[j+1] = flag[j] if len(flag[j]) > len(flag_[j+1]) else flag_[j+1]
#print(*flag)
res = sorted(flag,key=len,reverse=True)[0]

## OUT PUT
OUT = open("D:/Download/output.txt",mode='w')
OUT.write(res)
OUT.close()


'''
# 参考代码
# http://rosalind.info/problems/lcsq/
    
def lcs(s, t):
    s_length, t_length = len(s), len(t)
    
    if s_length == 0:
        return []
    elif s_length == 1:
        if s[0] in t:
            return [s[0]]
        else:
            return []
    else:
        i = s_length // 2
        s_beginning, s_end = s[:i], s[i:]
        
        ll_b = lcs_length(s_beginning, t)
        ll_e = lcs_length(s_end[::-1], t[::-1])
        _, k = max((ll_b[j] + ll_e[t_length - j], j) for j in range(t_length + 1))
        ## 取最大值对应的index
        t_beginning, t_end = t[:k], t[k:]
        
        return lcs(s_beginning, t_beginning) + lcs(s_end, t_end)
        ## 每次取一半的序列长度进行迭代
    
def lcs_length(s, t):
    current = [0] * (len(t)+1)

    ## 生成一个初始为0的列表 以及其复制 （current and prev）
    ## 双重循环 判断两个序列能够不连续顺序相同的最大数量

    for x in s:
        prev = list(current)
        for i, y in enumerate(t):
            if x == y:
                current[i + 1] = prev[i] + 1
            else:
                current[i + 1] = max(current[i], prev[i + 1])
    return current

if __name__ == '__main__':
    print ''.join(lcs("AACCTTGG", "ACACTGTGA"))
'''