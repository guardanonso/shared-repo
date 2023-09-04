# letter counter given an input word with some more stuff

while True:
    word = input("Enter a world: ")
    counter = 0 

    if word == "done":
        print("you are done!")
        break

    if word.find(" ") >= 0:
        print("Error, please enter just one word")
        continue

    elif word.isalpha() is False:
        print("Error, please enter a world")
        continue
    
    while counter < len(word):
        counter = counter + 1

    print(counter)


 
       