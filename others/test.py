hfile = open("romeo.txt")
counter = dict()

for line in hfile:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counter[word] = counter.get(word,0) + 1

lst = list()
for k,v in counter.items():
    tup = v,k
    lst.append(tup)

slst = sorted(lst,reverse=True)

for v,k in slst[:10]:
    print(k,v)
    








