hfile = open("mbox.txt")
dic = dict()

for line in hfile:
    line = line.rstrip()
    line = line.lower()
    if line.startswith("from ") is True:
        words = line.split()
        email = words[1]
        dic[email] = dic.get(email,0) + 1

lst = list()

for k,v in dic.items():
    tup = v,k
    lst.append(tup)

slst = sorted(lst, reverse = True)
for v,k in slst[:1]:
    print(k,v)


