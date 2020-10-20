import re,time
#from Bio import Phylo

st = time.time()
with open("D:/Download/rosalind_sptd.txt",mode='r') as f:
    taxas = f.readline().strip('\n').split()
    tree_texta = f.readline().strip('\n')[:-1]
    tree_textb = f.readline().strip('\n')[:-1]

    def trans2num(text):
        for i in range(len(taxas)):
            text = text.replace(taxas[i],str(i))
        return text
    
    texta,textb = map(trans2num,[tree_texta,tree_textb])
    del tree_texta,tree_textb

print("Use %s sec to read and preprocess data." %(time.time()-st))

pat = re.compile(r'\((\d+),(\d+)\)')
def get_min_clade(text):
    res = []
    for a,b in pat.findall(text):
        ##找到两个相连的叶
        res.append((a,b))
        res.append((b,a))
    return res

def expand_text(tagetloca):
    taget,loca = tagetloca
    if isinstance(taget,tuple):
        temp = "({},{})".format(taget[0],taget[1])
        if temp in loca:
            taget = temp
        else:
            taget = "({},{})".format(taget[1],taget[0])

    a,b = loca.split(taget)
    a = a[::-1]
    temp = 0 ; i = 0 ; ret = ''
    while temp != 1:
        if b[i] == '(':temp -= 1
        if b[i] == ')':temp += 1
        ret += b[i];i +=1 
    result = taget + ret

    temp = 0 ; i = 0 ; ret = ''
    while temp != -1:
        if a[i] == '(':temp -= 1
        if a[i] == ')':temp += 1
        ret += a[i]; i+= 1
    result = ret[::-1] + result
    return result

leaA,leaB = map(get_min_clade,[texta,textb])
scan_list = list(set(leaA) & set(leaB))
same_split = len(scan_list) // 2
rem = []
print("There are %s leaves to scan.."% same_split)
for lea in scan_list:
    while True:
        a , b = map(expand_text,[(lea,texta),(lea,textb)])
        if a == b:
            if a not in rem:
                rem.append(lea)
                same_split += 1
                lea = a
            else:break
        else:
            break
result = 2*(len(taxas) - 3 - same_split)
print("the program runs %s sec."%(time.time()-st))
print("All taxas: {} ; same split: {}".format(len(taxas),same_split))
print("The result is : ",result)