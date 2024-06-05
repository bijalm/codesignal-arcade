def solution(n):
    b = str(n)
    l = []

    for i in range(len(b)):
        x = int(b[:i] + b[i+1:])
        l.append(x)
        
    return (max(l))
