input = input("Enter a file name: ")
try:
    hfile = open(input)
except:
    print("Error, file does not exist")
    exit()

dic = dict()

for line in hfile:
    line = line.rstrip()
    line = line.lower()
    if line.startswith("from ") is True:
        words = line.split()
        email = words[1]
        stpoint = email.find("@")
        domain = email[stpoint:]
        print(domain)
        dic[domain] = dic.get(domain,0) + 1

hfile.close()
print(dic)
