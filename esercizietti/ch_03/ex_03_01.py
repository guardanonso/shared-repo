h = input("Enter Hours: ")
r = input("Enter Rate: ")
xh = float(h)
xr = float(r)

if xh > 40:
    print("Overtime")
    reg = 40 * xr
    otp = (xh - 40) * (xr*1.5)
    xp = reg + otp
    print("Pay:", xp)
else:
    print("Regular")
    reg = xh*xr
    print("Pay:",reg)






