from string import ascii_letters

def solution(inputString):
    sol = ""
    for i in inputString:
        if i == "z":
            sol += "a"
        else:
            sol += ascii_letters[ascii_letters.index(i) + 1]
            
            
    return sol
