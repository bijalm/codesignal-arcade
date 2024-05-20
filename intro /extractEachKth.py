def solution(inputArray, k):
    b = []
    for i in range(len(inputArray)):
        if (i+1) % k != 0:
            b.append(inputArray[i])
            
    return b
