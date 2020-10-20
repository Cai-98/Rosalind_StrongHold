para = open("D:/Download/rosalind_iprb.txt",mode="r")
k,m,n = [int(i) for i in para.read().split()]
s = k+m+n

print(
    1 - (n/s * (n-1)/(s-1) + 2*n/s*0.5*m/(s-1) + m/s*(m-1)/(s-1)*0.25)
)