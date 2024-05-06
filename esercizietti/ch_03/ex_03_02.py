# yes

h = input("Enter Hours: ")
r = input("Enter Rate: ")

try:
    xh = float(h)
    xr = float(r)
except:
    print("Error, please enter numeric input")
    quit()

if xh > 40:
    print("Overtime")
    reg = 40 * xr
    otp = (xh - 40) * (xr*1.5)
    xp = reg + otp
    print("Pay:", xp)
else:
    print("Regular")
    xp = xh*xr
    print("Pay:",xp)




