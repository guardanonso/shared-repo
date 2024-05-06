import re

with open("mbox.txt") as fhand:

    lst = list()
    for line in fhand:
        data = re.findall("New Revision: ([0-9]+)",line)
        print(data)
        if len(data):
            for k in data:
                k = int(k)
                lst.append(k)

avg = sum(lst)/len(lst)
print(round(avg))
        


        