hfile = open("mbox-short.txt")

for line in hfile:
    if line.startswith("From") is False:
        continue
    piece = line.split()
    if len(piece)>2:
        print(piece[2])

