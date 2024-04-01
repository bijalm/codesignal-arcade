def solution(a):
    if len(a) <= 1:
        return -1
        
    nonDup = set()
    
    for i in a:

        if i in nonDup:
            return i
        else:
            nonDup.add(i)        

    return -1
