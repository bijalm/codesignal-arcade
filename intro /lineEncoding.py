def solution(s):
    count = 1
    ans = ""
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        elif count == 1:
            ans += s[i-1]
            count = 1
        else:
            ans += str(count) + s[i-1]
            count = 1
    if count > 1:
        ans += str(count) + s[-1]
    else:
        ans += s[-1]    
    
    return ans
