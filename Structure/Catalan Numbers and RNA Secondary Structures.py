memorize = {} # 建立一个字典，存储已经出现过的字符串及不交叉完美匹配的数量
memorize[''] = 1 # 如果序列为空，说明只有这一种情况

def ismatch(c1, c2):
    """判断是否碱基配对的函数"""

    if (c1 == 'A' and c2 == 'U') or (c1 == 'U' and c2 == 'A') or \
            (c1 == 'G' and c2 == 'C') or (c1 == 'C' and c2 == 'G'):
        return 1
    else:
        return 0


def noncross(seq):
    """判断是否有不交叉的完美匹配"""

    if seq in memorize.keys(): # 如果这段序列之前已经被分析过了，直接取出结果即可
        return memorize[seq]

    if len(seq) % 2 == 1: # 如果这个序列长度是奇数，不可能存在完美匹配
        memorize[seq] = 0
        return 0

    if seq.count('A') != seq.count('U') or seq.count('G') != seq.count('G'): # 如果这个序列中配对的碱基数量不相同，不可能存在完美匹配
        memorize[seq] = 0
        return 0

    i = 1
    num = 0
    while i < len(seq): # 在序列中搜索所有可以与第一个碱基配对的碱基
        if ismatch(seq[0], seq[i]) == 1: # 如果第i个碱基配对
            num += (noncross(seq[1:i]) * noncross(seq[i+1:])) # 去检验被第k个碱基分出的两个序列
        i += 2 # 只需从第偶数个碱基中搜索
    memorize[seq] = num # 记录这个序列的不交叉完美匹配结果

    return num


f = open('D:/Download/rosalind_cat.txt', 'r')
input = f.readlines()
f.close()
index = input[0].replace('\n', '')
input = input[1:]
i = 0
seq = ''
while i < len(input):
    seq = seq + input[i].replace('\n', '')
    i += 1

res = noncross(seq)
print(res)
print(res % 1000000)