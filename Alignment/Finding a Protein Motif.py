import requests
from bs4 import BeautifulSoup
import re

def judge(s):
    if (s[0]=='N') and (s[1]!='P') and ((s[2] == 'S') or (s[2] == 'T')) and (s[3]!='P'):
        return True
    else :
        return False

pro = open("D:/Download/rosalind_mprt.txt",mode='r')
plist = {}
for line in pro.readlines():
    line = line.strip('\n')    
    r = requests.get("https://www.uniprot.org/uniprot/{0}.fasta".format(line)).text
    seq = ''
    lr = r.split('\n')
    for s in lr:
        s = s.strip('\n')
        if '>' in s:
            continue
        else:
            seq += s
    plist[line] = seq

find = {}
for name,seq in plist.items():
    pos = []
    for i in range(len(seq)-3):
        key = seq[i:i+4]
        if judge(key): pos.append(str(i+1))
    find[name] = pos

out = open("D:/Download/output.txt",mode='w')
for name, postion in find.items():
    if postion == []:
        continue
    out.write(name+'\n')
    out.write(' '.join(postion)+'\n')
out.close()