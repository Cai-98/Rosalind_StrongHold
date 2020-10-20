# http://rosalind.info/problems/pcov/

def get_superstring(collection):
    db = dict([(dna[:-1], dna[1:]) for dna in collection])
    k = list(db.keys())[0]
    superstring = ''
    
    while len(superstring) < len(collection):
        superstring += db[k][-1]
        k = db[k]
        
    return superstring

if __name__ == '__main__':
    collection = open('D:/Download/rosalind_pcov.txt').read().strip().split('\n')
    print(get_superstring(collection))