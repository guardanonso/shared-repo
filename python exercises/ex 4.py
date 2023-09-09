# Write a program to remove characters from a string starting from zero up to n and return a new string.

def remove_chars(word,chars):
    a = word[chars:]
    return(a)

while True:
    inpword = input("Choose a word: ")
    try:
        inpchars = int(input("How many characters you want to delete? "))
    except: 
        print("Please enter a number")
        continue
    length = len(inpword)
    if inpchars >= length:
        print("Choose a number of characters that's lower than the length of the that word you cho0se")
        continue
    else:   
        print(remove_chars(inpword,inpchars))

