file = input("Enter a file name: ")

try:
    hfile = open(file)
except:
    print("Error, this file does not exist")
    quit() 

for line in hfile:
    line = line.rstrip()
    print(line.upper())

