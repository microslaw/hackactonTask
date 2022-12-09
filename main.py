def countDifferences( word1:str, word2:str):
    differences = 0
    if(len(word1) == len(word2)):
        for letter1, letter2 in zip(word1,word2):
            if letter1 != letter2:
                differences +=1
    else:
        if(len(word1) < len(word2)):
            word1, word2 = word2, word1
        j = 0
        for i in range(len(word1)):
            if word1[i] == word2[j]:
                j+=1
            else:
                differences+=1
    return differences
    
def areTwoSwapped(toSwap:str, pattern):
    oddLetters = set()
    for letter1, letter2 in zip(toSwap, pattern):
        if letter1 != letter2:
            oddLetters.add(letter1, letter2)
    if len(oddLetters) == 2:
        return True
    return False