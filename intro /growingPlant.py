def solution(upSpeed, downSpeed, desiredHeight):
    day = 0
    night = 0
    count = 0
    while day < desiredHeight:
        day = (night + upSpeed)
        night = (day - downSpeed)
        count += 1
        
    return count
    
