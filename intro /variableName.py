def solution(name):
    if name[0].isdigit():
        return False
    for i in name:
        if not i.isalpha() and not i.isdigit() and i != '_':
            return False
            
    return True
