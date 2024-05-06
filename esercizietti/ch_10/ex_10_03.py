hfile = open(input())

dic = dict()
for line in hfile:
    line = line.lower()
    line = line.rstrip()
    line = line.replace(" ", "")
    for ch in line:
        if ch.isalpha() == False:
            continue
        dic[ch] = dic.get(ch,0)+1
lst= list()
for k, v in dic.items():
    tup = v,k
    lst.append(tup)
slst=sorted(lst,reverse=True)

for v,k in slst:
    print(k,v)