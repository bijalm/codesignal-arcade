def solution(inputArray):
    inputArray = sorted(inputArray)
    
    mVal = max(inputArray)
    i = 1
    while i <= mVal + 1:
        if all(x % i != 0 for x in inputArray):
            return i
            
        i += 1
