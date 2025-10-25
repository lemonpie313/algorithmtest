def solution(land):
    for i in range(1, len(land)):
        a0 = land[i][0] + max(land[i-1][1], land[i-1][2], land[i-1][3])
        a1 = land[i][1] + max(land[i-1][0], land[i-1][2], land[i-1][3])
        a2 = land[i][2] + max(land[i-1][1], land[i-1][0], land[i-1][3])
        a3 = land[i][3] + max(land[i-1][1], land[i-1][2], land[i-1][0])
        land[i][0], land[i][1], land[i][2], land[i][3] = a0, a1, a2, a3
        
    return max(land[-1])