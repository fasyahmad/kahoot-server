def writeFile():
    return "write" #writeJson

def readFile(fileLocation):
    theFile = open(fileLocation)
    data = json.load(theFile)
    return data

def checkFile():