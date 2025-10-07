from collections import deque

def solution(numbers, target):
    sums = 0
    n = 0
    cnt = []

    muls = []
    
    def dfs(sums, numbers, n, target, cnt):
        
        for mul in [1, -1]:
            muls.append(mul)
            added = sums + numbers[n] * mul
            if n!=len(numbers)-1:
                dfs(added, numbers, n+1, target, cnt)
            elif added == target:
                cnt.append(0)
            muls.pop()
    dfs(0, numbers, 0, target, cnt)  
            
    return len(cnt)