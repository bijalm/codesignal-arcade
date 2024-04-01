def solution(a, b):
    if a == b:
        return True
    
    differences = []
    
    for i in range(len(a)):
        if a[i] != b[i]:
            differences.append(i)
            
    if len(differences) != 2:
        return False
    else:
        return a[differences[0]] == b[differences[1]] and a[differences[1]] == b[differences[0]]
