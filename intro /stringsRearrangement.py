import itertools

def solution(inputArray):
    b = list(itertools.permutations(inputArray))
    for x in range(len(b)):
        for i in range(len(b[x])-1):
            if len(b[x][i]) != len(b[x][i+1]):
                break
            count = 0
            for j, k in zip(b[x][i], b[x][i+1]):
                if j != k:
                    count += 1
            if count != 1:
                break
        else:
            return True   
                    
    
    return False
