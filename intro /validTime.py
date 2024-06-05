def solution(time):
    s = time.split(':')
    if '00' <= s[0] < '24' and '00' <= s[1] <= '59':
        return True
    return False
