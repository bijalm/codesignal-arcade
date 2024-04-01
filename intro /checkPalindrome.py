def solution(inputString):
    outputString = ""
    for i in inputString[::-1]:
        outputString += i
    
    return inputString == outputString
