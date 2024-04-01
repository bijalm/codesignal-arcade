def solution(n):
    x = list(map(int, str(n)))
    y = len(x) // 2
    return sum(x[:y]) == sum(x[y:])
