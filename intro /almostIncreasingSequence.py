def solution(sequence):
    modifications = 0
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            modifications += 1
            if modifications > 1:
                return False
            if i > 0 and i < len(sequence) - 2 and sequence[i] >= sequence[i + 2] and sequence[i - 1] >= sequence[i + 1]:
                return False
    return True
