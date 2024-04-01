def solution(inputString):
    reverse = []
    
    for i in inputString:
        if i == ')':
            rev = ''
            while reverse and reverse[-1] != '(':
                rev += reverse.pop()
            reverse.pop()
            for r in rev:
                reverse.append(r)
        else:
            reverse.append(i)
            
    return ''.join(reverse)
    
