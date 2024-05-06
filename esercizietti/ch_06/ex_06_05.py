str = "X-DSPAM-Confidence: 0.8475 "
stpoint = str.find(":")

piece = str[stpoint+2:]
flpiece = float(piece)

print(piece,flpiece)