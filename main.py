from stats import getWordsCount, getCharacterFreq, getDictionaryList
import sys

def sort_on(list):
    return list['num']

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        fileContents = f.read()
        return fileContents

def printDictionaryList(list):
    for x in list:
        print(f'{x['char']}: {x['num']}')

def main():
    if len(sys.argv) == 1:
        print('Usage: python3 main.py <path_to_book>')
        exit(1)
    bookPath = sys.argv[1]
    fileContents = get_book_text(bookPath)
    totalWordCount = getWordsCount(fileContents)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {bookPath}...')
    print('----------- Word Count ----------')
    print(f'Found {totalWordCount} total words')
    charFreqDict = getCharacterFreq(fileContents)
    dictList = getDictionaryList(charFreqDict)
    dictList.sort(key=sort_on, reverse=True)
    print('--------- Character Count -------')
    printDictionaryList(dictList)

main()