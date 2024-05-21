def solution(inputString):
    prefix = ""
    for i in inputString:
        if i.isdigit():
            prefix += i
        else:
            break
    return prefix
