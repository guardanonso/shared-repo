# Write a program to remove characters from a string starting from zero up to n and return a new string.

while True:
    while True:
        word = input("Type a word: ")
        if word.isalpha()==False:
            continue
        else:   break
    chars = int(input("How many characters you want to remove? "))
    lenght = len(word)
    if chars>lenght:
        print("Select a number of character that's less than the lenght of the word")
        continue
    else:
        break

def remove_chars(word,chars):
    a = word[chars:]
    return(a)

if remove_chars(word,chars)=="":
    print("Resault: whole word cancelled")
else:
    print("Resault:",remove_chars(word,chars))