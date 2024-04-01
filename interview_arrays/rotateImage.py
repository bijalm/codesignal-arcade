import numpy as np
def solution(a):
    n = np.array(a)
    return np.rot90(n,3)
