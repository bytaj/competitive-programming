

def parseJson(stringToConvert):
    output = list()
    startString = False
    currentValue = ""
    for currentChar in stringToConvert:
        if currentChar == '\"':
            startString = not startString

    return [stringToConvert]
