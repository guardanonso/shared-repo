
file = input("Please Enter a file name: ")

try:
    hfile = open(file)
except:
    print("Error, couldn't find the file")
    quit()

counter = 0
sum = 0

for line in hfile:
    if line.startswith("X-DSPAM-Confidence: "):
        stpoint = line.find(":")
        piece = line[stpoint+2:]
        flpiece = float(piece)
        counter = counter + 1
        sum = sum + flpiece

print("Counter:",counter, "\n" "Sum:",sum,"\n" "Avarage spam confidence:", sum/counter)
        