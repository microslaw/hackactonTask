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

def numbersToLetters(word: str):
    numberLetterPairs = {"1":"i",
    "3": "e",
    "4": "a",
    "0": "o",
    "v": "u",
    "I": "l",
    "vv": "w",
    "ó":"u",
    "rz":"ż",
    "ch":"h"
    }
    for number in numberLetterPairs:
        word = word.replace(number, numberLetterPairs[number])
    return word

def deleteDuplicates(word:str):
    noDuplicatesWord = ""
    for i in range(len(word)-1):            
        if word[i] != word[i+1]:
            noDuplicatesWord+=word[i]
    noDuplicatesWord += word[-1]
    return word