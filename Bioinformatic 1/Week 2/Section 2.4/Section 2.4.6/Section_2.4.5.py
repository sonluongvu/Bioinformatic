# Input: Strings Pattern and Text as well as an integer d.
# Output: Countd(Text, Pattern).


from types import NoneType

# Read input
print('path for input files')
x = input()
x = str(x)
f = open(x, 'r')
strings_list = f.readlines()
print(strings_list, '\n')
pattern = strings_list[0].strip()
string_text = strings_list[1].strip()
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

# Write output to Output.txt
open('Bioinformatic 1/Week 2/Section 2.4.5/Output.txt', 'w').close() #Erase the previous output
with open('Bioinformatic 1/Week 2/Section 2.4.5/Output.txt', 'w') as output:
    output.write(str(mismatch_count(pattern, string_text, d)))

print(mismatch_count(pattern, string_text, d))