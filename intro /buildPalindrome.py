def solution(st):
    for i in range(len(st)):
        if st[i:] == st[i:][::-1]:
            return st + st[:i][::-1]

    return st
