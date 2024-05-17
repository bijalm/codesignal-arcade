from string import ascii_letters
def solution(cell1, cell2):
    let1 = ascii_letters.index(cell1[0])
    let2 = ascii_letters.index(cell2[0])
    
    if (let1 % 2 == let2 % 2) and (int(cell1[1]) % 2 == int(cell2[1]) % 2):
        return True
    if (let1 % 2 != let2 % 2) and (int(cell1[1]) % 2 != int(cell2[1]) % 2):
        return True
    return False
