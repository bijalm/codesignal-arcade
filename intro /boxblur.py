import numpy as np

def solution(image):
    solSizei = len(image) - 3 + 1
    solSizej = len(image[0]) - 3 + 1
    image = np.array(image)
    sol = np.zeros((solSizei, solSizej))
    
    for i in range(solSizei):
        for j in range(solSizej): 
            x = image[i:i+3, j:j+3]
            sol[i][j] = (x.sum() // 9)
            
    return sol
