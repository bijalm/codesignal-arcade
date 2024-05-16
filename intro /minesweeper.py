import numpy as np

def solution(matrix):
    sol = np.zeros((len(matrix), len(matrix[0])))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sol[i][j] = countMines(i, j, matrix)
    
    return sol
    
def countMines (x, y, matrix):
    mines = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny]:
                mines += 1
    return mines - matrix[x][y] if matrix[x][y] else mines
