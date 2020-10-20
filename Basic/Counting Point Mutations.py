DNA = open("D:/Download/rosalind_hamm.txt",mode="r")
s , t ,x= DNA.read().split("\n")
count = 0
for i in range(len(s)):
    if s[i] != t[i]:
        count += 1
print(count)
DNA.close()