IN = open("D:/Download/rosalind_tree.txt",mode='r')
node = IN.readline().strip('\n')
flag =['special'] + [0] * (int(node))
j = 1
for line in IN.readlines():
    line = line.strip('\n')
    s1,s2 = map(int,line.split())
    if (not flag[s1]) and (not flag[s2]):
        flag[s1] = flag[s2] = j
        j += 1
    elif flag[s1] and flag[s2]:
        t = flag[s1]
        for i in range(len(flag)):
            if flag[i] == t:
                flag[i] = flag[s2]
    elif flag[s1]:
        flag[s2] = flag[s1]
    elif flag[s2]:
        flag[s1] = flag[s2]
IN.close()
#print(flag)
zero = len(list(filter(lambda x: x == 0,flag)))
if zero - 1 < 1:
    zero = 1
print(len(set(flag))-2+zero-1)
