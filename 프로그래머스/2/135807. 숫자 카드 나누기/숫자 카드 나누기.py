import math
def solution(arrayA, arrayB):
    
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    
    for i in range(len(arrayA)):
        gcdA = math.gcd(gcdA, arrayA[i])
        gcdB = math.gcd(gcdB, arrayB[i])
        
    # print(str(gcdA) + " " + str(gcdB))
    
    bestA = 0
    bestB = 0
    
    for i in range(2, gcdA+1):
        if gcdA % i == 0:
            bb = True
            for j in arrayB:
                if j % i == 0:
                    bb = False
                    break
            if bb == True:
                bestA = i
        # print(i)
        # print(bestA)
    
    for i in range(2, gcdB+1):
        if gcdB % i == 0:
            aa = True
            for j in arrayA:
                if j % i == 0:
                    aa = False
                    break
            if aa == True:
                bestB = i
        # print(i)
        # print(bestB)
    
    answer = max(bestA, bestB)
    return answer