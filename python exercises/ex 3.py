# Write a program to accept a string from the user and display characters that are present at an even index number.

word = input("enter a word: ")

size = len(word)
print(size)
for i in range(0,size,2):
    print(word[i])
