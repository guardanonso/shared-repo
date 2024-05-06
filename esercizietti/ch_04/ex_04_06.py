#   kind of  useless program just practicing to create a proper function

def computepay(hours,rate):
    print("In computepay:",hours,rate)
    if hours > 40:
        reg = 40 * rate
        otp = (hours - 40) * (rate*1.5)
        pay = reg + otp
        
        
    else:
        pay = hours*rate

    return pay
        
h = input("Enter Hours: ")
r = input("Enter Rate: ")

try:
    xh = float(h)
    xr = float(r)
except:
    print("Error, please enter numeric input")
    quit()

xp = computepay(xh,xr)

print (xp)



 