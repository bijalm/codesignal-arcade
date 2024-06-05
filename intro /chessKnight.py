def solution(cell):
    s = 'abcdefgh'
    cellx = s.find(cell[0]) - s.find('a')
    celly = int(cell[1]) - 1
    
    x = [-1,1,2,2,1,-1,-2,-2]
    y = [2,2,1,-1,-2,-2,-1,1]
    
    count = 0
    for i in range(len(x)):
        if (0 <= cellx + x[i] < 8) and (0 <= celly + y[i] < 8):
            count += 1
            
    return count
