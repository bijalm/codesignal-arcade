def solution(inputArray, k):
    s = sum(inputArray[:k])
    m = s
    for i in range(k,len(inputArray)):
        s = s - inputArray[i-k] + inputArray[i]
        m = max(s, m)
        
    return m
