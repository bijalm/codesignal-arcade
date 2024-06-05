def solution(inputString):
    s = re.split(r'\D+', inputString)
    c = 0
    for i in s:
        if i.isdigit():
            c += int(i)

    return c
