def solution(n, firstNumber):
    pos = firstNumber + (n // 2)
    if pos < n:
        return pos
    elif pos > n:
        return pos - n
    else:
        return 0
