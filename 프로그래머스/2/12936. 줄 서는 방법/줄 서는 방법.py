import math

def solution(n, k):
    li = list(range(1, n + 1))
    arr = []
    k -= 1

    for i in range(n, 0, -1):
        print(k)
        fact = math.factorial(i - 1)  
        print(fact)
        idx = k // fact
        print(idx)
        arr.append(li.pop(idx))        
        k %= fact  
        print("--")

    return arr