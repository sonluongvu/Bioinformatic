# Input: Integers k and t, followed by a space-separated collection of strings Dna.
# Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.


# Import libraries:
import pandas as pd

# Input data:
x = input('path for input files: ')
input_file = open(str(x), 'r')
k_t = input_file.readline().split(' ')
k = k_t[0]
t = k_t[1]
dna = input_file.readline()

dna_1 = dna[0]
l = len(dna_1)

# Create a dataframe of k-mer from position i in dna list:
def motif_generator(dna, k, i):
    motif = []
    for dna_seq in dna:
        motif.append(dna_seq[i:i+k])
    df_motif = pd.DataFrame(motif)
    return df_motif

# Create a profile from a dataframe motif
def profile_generator(df_motif):
    for column in 