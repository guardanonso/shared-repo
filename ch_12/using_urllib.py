from urllib import request, error, parse

fhand = request.urlopen("https://it.wikipedia.org/wiki/Evgenij_Prigo%C5%BEin")



a = fhand.read().decode()
print(a)