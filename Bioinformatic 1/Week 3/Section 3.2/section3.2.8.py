# Input: Integers k and d, followed by a space-separated collection of strings Dna.
# Output: All (k, d)-motifs in Dna.

from types import NoneType

# Obtain input
print('path for input files:')
x = input()
input_file = open(str(x), 'r')
line_1 = input_file.readline()
line_2 = input_file.readline()
k_d = line_1.split(' ')
k_mer = int(k_d[0])
d = int(k_d[1])
dna = line_2.split(' ')

# Hamming distance function
def hamming_distance(string1, string2):
    count = 0
    l = len(string1)
    for i in range(l):
        if string1[i] != string2[i]:
            count += 1
    return count

# Neighbors function
def neighbors(pattern, d_num):
    nuc_list = {'A', 'C', 'G', 'T'}
    if d_num == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighborhood = set()
    suffixneighbors = neighbors(pattern[1:], d_num-1)
    for i in suffixneighbors:
        if hamming_distance(pattern[1:], i) < d_num:
            for nuc in nuc_list:
                neighborhood.add(nuc + i)
        else:
            neighborhood.add(pattern[0]+i)
    return neighborhood

# Find k_mer with at most d differences from a sequence
def pattern(sequence, k, d):
    l = len(sequence)
    k_mer_list = set()
    for i in range(l-k+1):
        pattern = sequence[i:i+k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            if neighbor not in k_mer_list:
                k_mer_list.add(neighbor)
    return k_mer_list
    

# Motif enumeration function
def motifenumeration(dna, k, d):
    patterns = set()
    k_mer_1 = pattern(dna[0], k, d)
    #print(*k_mer_1)
    for sequence in dna[1:]:
        k_mer_seq = pattern(sequence, k, d)
        for k_mer in k_mer_1:
            if k_mer in k_mer_seq:
                patterns.add(k_mer)
    return patterns

print(*motifenumeration(dna, k_mer, d))