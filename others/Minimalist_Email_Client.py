hfile = open("mbox-short.txt")
counter = 0
for line in hfile:
    line = line.lower()
    line = line.rstrip()
    if line.startswith("from ") is True:
        words = line.split()
        counter += 1
        print(words[1])
print("There were",counter,"lines in the file with from as the first word")
        
