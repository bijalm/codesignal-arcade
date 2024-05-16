def solution(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if inputArray[i] == elemToReplace else inputArray[i] for i in range(len(inputArray))]
