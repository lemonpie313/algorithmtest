from itertools import combinations
from collections import Counter

def solution(orders, courses):
    orderset = set()
    for i in range(len(orders)):
        orders[i] = list(orders[i])
        for order in orders[i]:
            orderset.add(order)
    orderset = list(orderset)
    
    result = []
    
    for coursenum in courses:
        counter = Counter()

        for order in orders:
            for combo in combinations(sorted(order), coursenum):
                counter[combo] += 1
        
        num = -1
        for commons in counter.most_common():
            if commons[1] < 2:
                break
            elif num == -1:
                num = commons[1]
            elif num > commons[1]:
                break
                
            commonmenu = list(commons[0])
            commonmenu.sort()
            commonmenus = "".join(commonmenu)
        
            result.append(commonmenus)
        
    result.sort()
                    
    return result