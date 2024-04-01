def solution(s):
    for i in s:
        ind = s.find(i, s.find(i)+1)
        if ind == -1:
            return i
            
    return '_'
