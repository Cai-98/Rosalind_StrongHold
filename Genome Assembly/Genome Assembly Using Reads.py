from Bio.Seq import reverse_complement as rc

def assemble(k, reads):
    kmers = set([read[i:i+k] for read in reads for i in range(len(read)-k+1) ])
    assembly = kmers.pop()
    while len(kmers) > 0:
        extensions = [ c for c in "ACTG" if assembly[-(k-1):] + c in kmers ]
        if len(extensions) != 1:
            break
        assembly += extensions[0]
    is_cyclic = assembly[-(k-1):] == assembly[:k-1]
    if is_cyclic: 
        assembly = assembly[:-(k-1)]
        return assembly
    return None

if __name__ == '__main__':
    reads = open('D:/Download/rosalind_asmq.txt').read().strip().split('\n')
    
    reads += [rc(read) for read in reads]
    k = len(reads[0])
    while (k > 0):
        s = assemble(k, reads)
        if s != None:
            print (s)
            break
        k -= 1

