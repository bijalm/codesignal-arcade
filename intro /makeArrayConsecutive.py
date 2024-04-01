def solution(statues):
    #make statues into ascending order
    statues.sort()
    #get first and last number
    firstNum = statues[0]
    lastNum = statues[-1]
    #compare list with range of first to lastNum and count missed numbers
    missing = 0
    for i in range(firstNum, lastNum+1):
        if(i != 0):
            if(i not in statues):
                missing += 1
    
    return missing
