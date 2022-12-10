import censoring


while True:
    word = input("Input board to see if it is a curse \n")
    if (censoring.isABadWord(word)):
        print( word, "is a curse")
    else:
        print(word, "isn't a curse")