from collections import defaultdict

def solution(s):
    d = defaultdict(int)
    
    for i in s:
        d[i] += 1
        
    return len(d.keys())    

