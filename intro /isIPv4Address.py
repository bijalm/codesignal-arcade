def solution(inputString):
    a = inputString.split('.')
    if len(a) == 4:
        for i in a:
            if not i.isdigit():
                return False
            x = int(i)
            if x < 0 or x > 255 or i == '0' + str(x):
                return False
                
        return True
    
    return False
