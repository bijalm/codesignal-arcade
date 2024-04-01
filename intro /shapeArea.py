def solution(n):
    area = 0
    for i in range(1, n+1):
        area += (2*i - 1)
        
    if (n != 1):
        for i in range(1, n):
            area += (2*i - 1)
    
    return area
