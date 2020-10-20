n = int(input("Input The Num of leaves: "))
res = [1,1]
MODULO = 1000000
while len(res) < n:
    res.append((2*len(res)-1)*res[-1])

print(res[-2]%MODULO) 
# while Counting Rooted Binary Trees: It is res[-1]
