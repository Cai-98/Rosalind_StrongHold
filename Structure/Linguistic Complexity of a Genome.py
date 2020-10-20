from numba import jit

@jit(nopython = True)
def max_sub(n):
    count = 0
    k = 1;a=4
    while k < n+1 and a**k < n-k+1:
        count += a**k
        k += 1
    while k < n+1:
        count += n-k+1
        k += 1
    return count

with open("D:/Download/rosalind_ling.txt",mode='r') as f:
    s = f.readline().strip()

def longest_common_prefixes(s, suffix_array):
    lcp = [0]*len(s)
    rank = [0]*len(s)
    for i in range(len(s)):
        rank[suffix_array[i]] = i

    h = 0
    for i in range(len(s)):
        if rank[i] > 0:
            k = suffix_array[rank[i]-1]
            while s[i+h] == s[k+h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp[1:]

def sub(s):
    s += '$'
    suffixes = sorted([(i, s[i:]) for i in range(len(s))], key=lambda x:x[1])
    suffix_array = list(zip(*suffixes))[0]
    lcp = longest_common_prefixes(s, suffix_array)
    n = len(s) - 1
    count = 0
    for i in range(len(lcp)):
        count += n - suffix_array[i+1] - lcp[i]
    return count

def ling(s):
    n = len(s)
    print(sub(s) / (max_sub(len(s))))

ling(s)