from collections import Counter
def solution(topping):
    answer = 0
    cakeB = {}
    cakeA = Counter(topping)
    
    for i in topping:
        if i in cakeB.keys():
            cakeB[i] += 1
        else:
            cakeB[i] = 1
        cakeA[i] -= 1
        if cakeA[i] == 0:
            del cakeA[i]
        if len(cakeA.keys()) == len(cakeB.keys()):
            answer += 1
    return answer