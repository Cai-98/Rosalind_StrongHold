
with open("D:/Download/rosalind_ebin.txt",mode='r') as f:
    N = int(f.readline().strip('\n'))
    A = list(map(float,f.readline().strip('\n').split()))

R = [N*i for i in A]
print(*R)