input = input("Enter a file name: ")
try:
    hfile = open(input)
except:
    print("Error, file does not exist")
    exit()

counter1 = dict()
counter2 = dict()

for line in hfile:
    line = line.rstrip()
    line = line.lower()
    
    if line.startswith("from ") is True:
        words = line.split()
        day = words[2]
        email = words[1]
        counter1[day] = counter1.get(day,0) + 1
        counter2[email] = counter2.get(email,0)+1

hfile.close()

largestnum = None
largestmail = None

for (k,v) in counter2.items():
    if largestnum is None or v > largestnum:
        largestnum = v
        largestmail = k

lst = list()
for k,v in counter2.items():
    lst.append((v,k))

lst.sort(reverse=True)
print(lst)

for v,k in lst[:1]:
    print(k,v)
    

    
# print(counter1)
# print(counter2)
# print(largestmail,largestnum)