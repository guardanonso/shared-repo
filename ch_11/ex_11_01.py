import re

fhand = open("mbox.txt")
input = input("Enter a regular expression: ")

counter = 0
for line in fhand:
    if re.search(input,line):
        counter += 1

print(counter)



