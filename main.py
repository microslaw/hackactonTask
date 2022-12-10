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

def normalizeChars(word: str):
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


def deleteDuplicates(word:str):
    noDuplicatesWord = ""
    for i in range(len(word)-1):            
        if word[i] != word[i+1]:
            noDuplicatesWord+=word[i]
    noDuplicatesWord += word[-1]
    return word


def formatEndings(word:str):
    formatList = {"ana":"any",
    "anie": "any",
    "ać": "any",
    "aż": "any",
    "ał": "any",
    "ony": "any",
    }

    for ending in formatList:
        if word[-len(ending):] == ending:
            word = word.rstrip(ending) + formatList[ending]
    return word


def formatWord(word:str):
    formattedWord = normalizeChars(word)
    formattedWord = deleteDuplicates(formattedWord)
    formattedWord = formattedWord.lower()
    formattedWord = formatEndings(formattedWord)
    return formattedWord


def isABadWord(word:str):
    for badWord in badWordsList:
        badWord = formatWord(badWord)
        word = formatWord(word)
        differencesCount = countDifferences(word, badWord)
        if differencesCount == 0:
            return True
        if differencesCount == 1 and (len(word) -1 == len(badWord)):
            return True
        if differencesCount == 2 and (len(word) == len(badWord)):
            return True
    return False


def readFile(filename:str):
    lines = []
    with open(filename, 'r', encoding='utf-8') as rfile:
        for line in rfile:
            line = line.strip()
            words = line.split(" ")                
            lines.append(words)
    return lines


def censorWord(word:str):
    if isABadWord(word):
        word = word[0] + ('*'*(len(word)-2)) + word[-1]
    return

badWordsList = readFile("badWords.txt")

