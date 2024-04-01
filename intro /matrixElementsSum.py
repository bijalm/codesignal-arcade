def solution(matrix):
    cost = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0:
                if matrix[i][j] != 0:
                    cost += matrix[i][j]
            else:
                haunted = False
                for x in range(0, i):
                    if matrix[x][j] == 0:
                        haunted = True
                        
                if not haunted and matrix[i][j] != 0:
                    cost += matrix[i][j]
                    
    return cost
