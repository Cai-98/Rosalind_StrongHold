def ismatch(c1, c2):
    """判断是否碱基配对的函数"""

    if (c1 == 'A' and c2 == 'U') or (c1 == 'U' and c2 == 'A') or \
            (c1 == 'G' and c2 == 'C') or (c1 == 'C' and c2 == 'G'):
        return 1
    else:
        return 0
memorize = {}
memorize[''] = 1
def noncross(seq):
    """判断是否有不交叉的完美匹配"""

    if seq in memorize.keys(): # 如果这段序列之前已经被分析过了，直接取出结果即可
        return memorize[seq]
    if len(seq) == 1:
        return 1
    i = 1
    num = noncross(seq[1:]) 
    while i < len(seq): # 在序列中搜索所有可以与第一个碱基配对的碱基
        if ismatch(seq[0], seq[i]) == 1: # 如果第i个碱基配对
            num += (noncross(seq[1:i]) * noncross(seq[i+1:])) # 去检验被第k个碱基分出的两个序列
        i += 1
    memorize[seq] = num # 记录这个序列的不交叉完美匹配结果

    return num

with open("D:/Download/rosalind_motz.txt",mode='r') as f: # rosalind_motz
    seq = ''
    head = f.readline()
    for line in f.readlines():
        seq += line.strip('\n')
print(noncross(seq)%1000000)