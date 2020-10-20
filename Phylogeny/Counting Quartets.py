
with open("D:/Download/rosalind_cntq.txt",mode='r') as f:
    n = int(f.readline().strip('\n'))
    tree_text = f.readline().strip('\n')[:-1]
def pow(n):
    ret = 1
    for i in range(1,n+1):
        ret*=i
    return ret

res = int(pow(n)/((pow(4)*pow(n-4)))) % 1000000
print(res)