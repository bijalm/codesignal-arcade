from collections import defaultdict

def solution(inputString):
    charCount = defaultdict(int)
    
    for i in inputString:
        charCount[i] += 1
        
    oddCount = 0
    for k,v in charCount.items():
        if v % 2 != 0:
            oddCount += 1
        if (len(inputString) % 2 != 0 and oddCount > 1) or (len(inputString) % 2 == 0 and oddCount > 0):
            return False
        
        
    return True
  
