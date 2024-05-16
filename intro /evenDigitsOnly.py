def solution(n):
    while n != 0:
        if (n % 10) % 2 != 0:
            return False
        n //= 10
    return True
