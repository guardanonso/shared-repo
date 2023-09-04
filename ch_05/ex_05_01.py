# given various digits, return avarage of theese

sum = 0
count = 0
avg = None

while True:
    num = input("Please enter a number: ")
    if num == "done":
        print("You are done.","Final resaults:","Sum:",sum,"Count:",count,"Avarge:",avg)
        break
    try:
        xnum = float(num)
    except:
        print("Invalid input")
        continue

    sum = sum + xnum
    count = count + 1
    avg = sum/count
    print("Sum:",sum,"Count:",count,"Avarage:",avg)
         
        








