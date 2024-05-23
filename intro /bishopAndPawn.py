from string import ascii_letters

def solution(bishop, pawn):
    let1 = ascii_letters.index(bishop[0])
    let2 = ascii_letters.index(pawn[0])
    
    sameColor = False
    if (let1 % 2 == let2 % 2) and (int(bishop[1]) % 2 == int(pawn[1]) % 2):
        sameColor = True
    if (let1 % 2 != let2 % 2) and (int(bishop[1]) % 2 != int(pawn[1]) % 2):
        sameColor = True
        
    if sameColor and (let1 != let2) and (bishop[1] != pawn[1]) :
        return True
        
    return False
