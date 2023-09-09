import re

lst = list()

while True:
    a = input("Enter a number to add it to a list: ")
    if a.lower() == "done":
        break
    elif re.search("[A-Za-z]+",a):
        print("Please enter a number")
        continue
    elif re.search("\s+",a):
        print("Please enter just one number")
        continue
    lst.append(a)
    continue

def list_checker(lsst):
    if type(lsst) is list:
        stpoit = lsst[0]
        endpoint = lsst[-1]
        if stpoit == endpoint:
            return(True)
        else:
            return(False)
        
print(list_checker(lst))
        
    

