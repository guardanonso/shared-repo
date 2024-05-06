fhand = open("mbox-short.txt")

dic = dict()
for line in fhand:
    line = line.lower()
    if line.startswith("from ") is True:
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        dic[hour] = dic.get(hour,0)+1

lst = list()

for k,v in dic.items():
    tup = k,v
    lst.append(tup)

slist = sorted(lst)

print(slist)





        
        
    
        