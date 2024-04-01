def solution(a):
    noTree = []
    for i in a:
        if i != -1:
            noTree.append(i)
            
    noTree = sorted(noTree)
    j = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = noTree[j]
            j += 1
    
    return a
