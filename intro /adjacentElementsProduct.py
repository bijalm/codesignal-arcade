import math
def solution(inputArray):
    maxNum = -math.inf
    temp = 0
    for i in range(0, len(inputArray)-1):
        if(i < len(inputArray)):
            temp = inputArray[i] * inputArray[i+1]
            if(temp >= maxNum):
                maxNum = temp
    return maxNum
