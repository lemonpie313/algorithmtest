import heapq
from collections import deque
def solution(maps):
    maps = [list(maps[i]) for i in range(len(maps))]
    
    hpp = []
    
    def dfs(maps, start, sums):
        queue = deque([])
        queue.append(start)
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        
        while queue:
            loc = queue.popleft()
            if maps[loc[0]][loc[1]] != "X":
                sums += int(maps[loc[0]][loc[1]])
                maps[loc[0]][loc[1]] = "X"
                
                for i in range(4):
                    newloc = [loc[0] + dx[i], loc[1] + dy[i]]
                    if 0 <= newloc[0] < len(maps) and 0 <= newloc[1] < len(maps[0]):
                        queue.append(newloc)
                
        return sums
            
        # 어쟀거나 dfs로 결과 합...
        
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != "X":
                heapq.heappush(hpp, dfs(maps, [i, j], 0))
    
    answer = []
    if not hpp:
        return [-1]

    while hpp:
        answer.append(heapq.heappop(hpp))
    
    return answer