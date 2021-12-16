# Read .txt file
f = open('Bioinformatic 1/Week 1/dataset_2_6.txt','r')
content = f.readlines()
#print(content)

# Pattern counter function
def patterncount(text, pattern):
    l = len(text)
    t = len(pattern)
    count = 0
    for i in range(l):
        if pattern == text[i:i+t]:
            count = count + 1
    return count

# Print result
print('Number of pattern is', patterncount(content[0].strip(), content[1].strip()))

# .strip is to remove '\n'