def solution(inputArray):
    diff = []
    
    for i in range(len(inputArray) - 1):
        diff.append(abs(inputArray[i]-inputArray[i+1]))
        
    return max(diff)
