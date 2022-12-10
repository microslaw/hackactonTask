def __countDifferences( word1:str, word2:str):
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
            if word1[min(i,len(word1)-1)] == word2[min(j,len(word2)-1)]:
                j+=1
            else:
                differences+=1
    return differences
    
def __areTwoSwapped(toSwap:str, pattern):
    oddLetters = set()
    for letter1, letter2 in zip(toSwap, pattern):
        if letter1 != letter2:
            oddLetters.add(letter1, letter2)
    if len(oddLetters) == 2:
        return True
    return False

def __normalizeChars(word: str):
    normalizingChars = {"1":"i",
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
    for number in normalizingChars:
        word = word.replace(number, normalizingChars[number])
    return word


def __deleteDuplicates(word:str):
    noDuplicatesWord = ""
    for i in range(len(word)-1):            
        if word[i] != word[i+1]:
            noDuplicatesWord+=word[i]
    noDuplicatesWord += word[-1]
    return word


def __formatEndings(word:str):
    formatList = {"ana":"any",
    "anie": "any",
    "ać": "any",
    "aż": "any",
    "ał": "any",
    "ony": "any",
    "o":"a",
    "y":"a"
    }

    for ending in formatList:
        if word[-len(ending):] == ending:
            word = word.rstrip(ending) + formatList[ending]
    return word


def __formatWord(word:str):
    formattedWord = __normalizeChars(word)
    formattedWord = __deleteDuplicates(formattedWord)
    formattedWord = formattedWord.lower()
    formattedWord = __formatEndings(formattedWord)
    return formattedWord


badWordsList = []
with open("badWords.txt", 'r', encoding='utf-8') as rfile:
    for line in rfile:
        line = line.strip()                
        badWordsList.append(line)

    

def isABadWord(word:str):
    if len(word)<3:
        return
    for badWord in badWordsList:
        badWord = __formatWord(badWord)
        word = __formatWord(word)
        differencesCount = __countDifferences(word, badWord)
        if differencesCount == 0:
            return True
        if differencesCount == 1 and (len(word) -1 == len(badWord)):
            return True
        if differencesCount == 2 and (len(word) == len(badWord)):
            return True
    return False

def censorWord(word:str):
    if isABadWord(word):
        word = word[0] + ('*'*(len(word)-2)) + word[-1]
    return word

