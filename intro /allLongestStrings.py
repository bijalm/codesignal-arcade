from collections import defaultdict

def solution(inputArray):
    lengths = defaultdict(list)
    
    for i in inputArray:
        lengths[len(i)].append(i)
                   
    return lengths[max(lengths)]
