# Input: A string Text as well as integers k and d.
# Output: All most frequent k-mers with up to d mismatches in Text.

from types import NoneType

# Obtain input
print('path for input files:')
x = input()
x = str(x)
f = open(x, 'r')
strings_list = f.readlines()
text = strings_list[0].strip()
k = int(strings_list[1].strip())
d = int(strings_list[2].strip())


# Hamming distance function
def hamming_distance(string1, string2):
    count = 0
    l = len(string1)
    for i in range(l):
        if string1[i] != string2[i]:
            count += 1
    return count

# Mismatch counting function:
def mismatch_count(string_pattern, text, num_d):
    l_text = len(text)
    l = len(string_pattern)
    position = []
    for i in range(l_text-l+1):
        hamming_num = hamming_distance(string_pattern, text[i: i+l])
        if hamming_num <= d:
            position.append(i)
    return len(position)

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

# Frequent words with mismatch
def frequent_words_with_mismatch(genome, k_mer, d_mismatch):
    patterns = []
    freqmap = {}
    n = len(genome)
    for i in range(n-k+1):
        pattern = genome[i : i+k]
        neighborhood = neighbors(pattern, d_mismatch)
        #print(neighborhood)
        #print(pattern)
        for neighbor in neighborhood:
            #print(neighbor)
            if neighbor not in freqmap:
                freqmap[neighbor] = 1
            else:
                freqmap[neighbor] += 1
            #print(freqmap)
    #print(freqmap)
    m = max(freqmap, key= freqmap.get)
    print(m)
    for pattern in freqmap:
        if freqmap[pattern] == m:
            patterns.append(pattern)
    return patterns

print(*frequent_words_with_mismatch(text, k, d))