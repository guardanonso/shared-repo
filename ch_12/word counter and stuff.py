from urllib.request import urlopen

with urlopen("http://data.pr4e.org/romeo.txt") as response:
    body = response.read()
    decoded_body = body.decode()


lines = decoded_body.splitlines()
word_counter = dict()
for line in lines:
    words = line.split()
    for word in words:
        word_counter[word] = word_counter.get(word,0) + 1

lst = list()
for k,v in word_counter.items():
    tup = (v,k)
    lst.append(tup)

print(sorted(lst))



    