
with open("D:/Download/rosalind_seto.txt",mode='r') as f:
    num = int(f.readline().strip('\n'))
    U = set(range(1,num+1))
    set1 = eval(f.readline().strip('\n'))
    set2 = eval(f.readline().strip('\n'))

with open("D:/Download/out.txt",mode='w') as f:
    f.write(str(set1|set2) + '\n')
    f.write(str(set1&set2) + '\n')
    f.write(str(set1-set2) + '\n')
    f.write(str(set2-set1) + '\n')
    f.write(str(U - set1) + '\n')
    f.write(str(U - set2))