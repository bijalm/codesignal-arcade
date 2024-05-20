def solution(a):

    closest = []
    for i in a:
        x = sum(abs(b - i) for b in a)
        closest.append(x)
        
    ind = closest.index(min(closest))
    
    return a[ind]
