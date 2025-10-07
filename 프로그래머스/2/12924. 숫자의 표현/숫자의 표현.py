import math
def solution(n):
    n = n * 2
    cnt = 0
    a = []
    sqr = math.floor(math.sqrt(n))
    for i in range(1, sqr+1):
        if (n%i == 0) and (n/i != i) and (i%2 != (n/i)%2):
            a.append(i)
            cnt+=1
    return cnt