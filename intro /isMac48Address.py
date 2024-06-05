def solution(inputString):
    a = inputString.split('-')
    if len(a) == 6:
        valid_chars = set('0123456789ABCDEF')
        return all(len(i) == 2 and i[0] in valid_chars and i[1] in valid_chars for i in a)
    return False
