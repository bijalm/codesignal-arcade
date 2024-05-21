def solution(n):
    count = 0
    while n >= 10:
        temp = n
        s = 0
        while temp != 0:
            s += (temp % 10)
            temp //= 10
            
        n = s
        count += 1
        
    return count
