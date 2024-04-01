def solution(picture):
    pic = []
    pic.append("*" * (len(picture[0]) + 2))
    
    for i in picture:
        pic.append("*" + i + "*")
        
    pic.append("*" * (len(picture[0]) + 2))
    
    return pic 
