def countWordsFromFile():
    fileName = input("enter the file name")
    numberOfWords = 0
    openFile = open(fileName)
    for I in openFile:
        words=I.split()
        numberOfWords += len(words)
    print("numberOfWords")
    print(numberOfWords)
countWordsFromFile()