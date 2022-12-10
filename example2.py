import censoring

while True:
    line = input("Input a sentence to censor it's curse words: \n")
    words = line.split(" ")
    for word in words:
        print(censoring.censorWord(word), end=" ")
        print()
