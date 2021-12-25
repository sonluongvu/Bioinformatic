# Input: An integer k, followed by a space-separated collection of strings Dna.
# Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers. (If there are multiple such strings Pattern, then you may return any one.)


# Obtain input
print('path for input files:')
x = input()
input_file = open(str(x), 'r')
k = int(input_file.readline())
dna = input_file.readline().split(' ')

# Hamming distance function
def hamming_distance(string1, string2):
    count = 0
    l = len(string1)
    for i in range(l):
        if string1[i] != string2[i]:
            count += 1
    return count

# Find hamming distance between k-mer and a dna_seq:
def find_distance(k_mer, dna_seq):
    l = len(dna_seq)
    k = len(k_mer)
    distance = hamming_distance(k_mer, dna_seq[0:k])
    for i in range(l-k+1):
        if hamming_distance(k_mer, dna_seq[i:i+k]) < distance:
            distance = hamming_distance(k_mer, dna_seq[i:i+k])
    return distance

# Generator list of k_mer:
def generate_dna_kmers(k):
    # this code is from: "https://classes.cs.uchicago.edu/archive/2020/fall/30121-1/lecture-examples/Kmers/Kmers.html"
    bases = ["A", "C", "T", "G"]
    last = bases
    current = []
    for i in range(k-1):
        for b in bases:
            for l in last:
                current.append(l+b)
        last = current
        current= []
    return last

# sum of hamming distance between k-mer and a dna_seq list:
def sum_distance(k_mer, dna):
    sum = 0
    for dna_seq in dna:
        sum += find_distance(k_mer, dna_seq)
    return sum



def median_string(dna, k):
    k_mer_list = generate_dna_kmers(k)
    distance = sum_distance(k_mer_list[0], dna)
    median = ''
    for k_mer in k_mer_list:
        if distance > sum_distance(k_mer, dna):
            distance = sum_distance(k_mer, dna)
            median = k_mer
    return median

print(median_string(dna, k))
