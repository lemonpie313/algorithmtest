def solution(numbers, target):
    
    def dfs(sums, n):
        if n == len(numbers):
            if sums == target:
                return 1
            else:
                return 0
        plus = dfs(sums + numbers[n], n+1)
        minus = dfs(sums - numbers[n], n+1)
        
        return plus + minus

    return dfs(0, 0)