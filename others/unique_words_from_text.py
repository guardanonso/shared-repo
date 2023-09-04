hfile = open("romeo.txt")

uniquewords = list()

for line in hfile:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in uniquewords:
            uniquewords.append(word)
            
uniquewords.sort()
print(uniquewords)





