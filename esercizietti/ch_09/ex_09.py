fname = "mbox-short.txt"

hfile = open(fname)
p = dict()
for line in hfile:
    line = line.rstrip()
    words = line.split()
    for word in words:
        p[word] = p.get(word,0) + 1

bigword = None
bigfrequency = None

for key,value in p.items():
    if bigfrequency is None or value > bigfrequency:
        bigword = key
        bigfrequency = value

print(bigword,bigfrequency)




        
        

        