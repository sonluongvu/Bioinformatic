# input: Two strings of equal length
# output: The hamming distance between these strings

# read input

f = open('Bioinformatic 1/Week 2/Section 2.4.3/dataset_9_3.txt', 'r')
strings_list = f.readlines()
string_1 = strings_list[0].strip()
string_2 = strings_list[1].strip()
#print(string_1, '\n')
#print(string_2, '\n')

# Length of input string
l = len(string_1)

# Calculating hamming distance of two strings:
def hamming_distance(string1, string2):
    count = 0
    for i in range(l):
        if string1[i] != string2[i]:
            #print(string_1[i],'\n')
            #print(string_2[i],'\n')
            count += 1
            #print(count,'\n')
    return count

# Print result:
print('Hamming distance are', hamming_distance(string_1, string_2))