import string

def solution(inputString):

    count = dict.fromkeys(string.ascii_lowercase, 0)
    
    for i in inputString:
        count[i] += 1
    
    keys = list(count.keys())
    
    for i in range(1, len(keys)):
        if count[keys[i-1]] < count[keys[i]]:
            return False
            
    return True
