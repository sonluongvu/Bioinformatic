# Input: Integers k and t, followed by a space-separated collection of strings Dna.
# Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.


# Import libraries:
import pandas as pd

# Input data:
x = input('path for input files: ')
input_file = open(str(x), 'r')
k_t = input_file.readline().split(' ')
k = int(k_t[0])
t = int(k_t[1])
dna = input_file.readline()

# Create a motif dataframe of k-mer from position i in dna list:
def motif_generator(dna, k, i):
    motif = []
    for dna_seq in dna:
        motif.append(list(dna_seq[i:i+k]))
    df_motif = pd.DataFrame(motif)
    return df_motif

# Create a profile from a dataframe motif
def profile_generator(df_motif):
    profile = []
    for index_column in range(k):
        A_count = 0.0
        C_count = 0.0
        G_count = 0.0
        T_count = 0.0
        for index_row in df_motif.shape(0):
            if df_motif.iloc[index_row, index_column] == 'A':
                A_count += 1.0
            elif df_motif.iloc[index_row, index_column] == 'C':
                C_count += 1.0
            elif df_motif.iloc[index_row, index_column] == 'G':
                G_count += 1.0
            else:
                T_count += 1.0
        A_count = A_count/t
        C_count = C_count/t
        G_count = G_count/t
        T_count = T_count/t
        profile.append([A_count, C_count, G_count, T_count])
    df_profile = pd.DataFrame(profile)
    return df_profile

# Find the median string from a profile DataFrame:
def median_string(df_profile):
    profile_k_mer = []
    for index_column in df_profile:
        max_nuc_pos = index_column.index(max(index_column))
        if max_nuc_pos == 0:
            profile_k_mer.append('A')
        elif max_nuc_pos == 1:
            profile_k_mer.append('C')
        elif max_nuc_pos == 2:
            profile_k_mer.append('G')
        else:
            profile_k_mer.append('T')
    return str(profile_k_mer)

# Greedy motif search:
def greedy_motif_search(dna, k, t):
    best_motif = []
    l = len(dna[0])
    for i in range(l-k+1):
        df_motif = motif_generator(dna, k, i)
        df_profile = profile_generator(df_motif)
        k_mer = median_string(df_profile)
        best_motif.append(k_mer)
    return best_motif

print(*greedy_motif_search(dna, k, t))