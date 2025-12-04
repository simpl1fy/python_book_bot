def getWordsCount(story):
    wordCount = len(story.split())
    return wordCount

def getCharacterFreq(story):
    wordFrequency = {}
    for c in story:
        char = c.lower()
        if char in wordFrequency:
            freq = wordFrequency[char]     # Get the current frequency of the character
            wordFrequency.update({char: freq+1})
        else:
            wordFrequency[char] = 1
    return wordFrequency

def getDictionaryList(dict):
    dictList = []
    for x in dict:
        dataDict = {}
        if x.isalpha():
            dataDict["char"] = x
            dataDict["num"] = dict[x]
            dictList.append(dataDict)
        else:
            continue
    return dictList