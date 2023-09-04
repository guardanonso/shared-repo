nums = list()

while True:
    try:
        num = input("Enter a number: ")
    except:
        print("Eror, please enter a number")
    if num == "done":
        print("It's done!")
        print("Maximum:",max(nums),"Minumum:", min(nums) )
        break
    fnum = float(num)
    nums.append(fnum)
