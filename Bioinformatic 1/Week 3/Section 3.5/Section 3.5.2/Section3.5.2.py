# Input: A string Text, an integer k, and a 4 × k matrix Profile.
# Output: A Profile-most probable k-mer in Text.

# Obtain input
x = input('path for input files: ')
input_file = open(str(x), 'r')
dna_seq = str(input_file.readline())
k = int(input_file.readline())
A_profile = input_file.readline().split(' ')
C_profile = input_file.readline().split(' ')
G_profile = input_file.readline().split(' ')
T_profile = input_file.readline().split(' ')

def find_pr(dna_seq, k, A_profile, C_profile, G_profile, T_profile):
    l = len(dna_seq)
    most_pr_k_mer = dna_seq[0:k]
    max_k_mer_pr = 0
    for i in range(l-k+1):
        k_mer = dna_seq[i:i+k]
        k_mer_pr = 1.0
        for pos in range(k):
            nuc = list(k_mer)[pos]
            if nuc == 'A':
                k_mer_pr *= float(A_profile[pos])
            elif nuc == 'C':
               k_mer_pr *= float(C_profile[pos])
            elif nuc == 'G':
                k_mer_pr *= float(G_profile[pos])
            else:
                k_mer_pr *= float(T_profile[pos])
        if k_mer_pr > max_k_mer_pr:
            max_k_mer_pr = k_mer_pr
            most_pr_k_mer = k_mer
    return most_pr_k_mer

print(find_pr(dna_seq, k, A_profile, C_profile, G_profile, T_profile))