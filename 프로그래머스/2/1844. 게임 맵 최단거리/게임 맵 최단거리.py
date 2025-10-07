# BFS 최단거리 2차원 배열
from collections import deque

def solution(maps):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n, m = len(maps), len(maps[0])
    
    visited = set([(0, 0)])
    queue = deque([(0, 0, 1)])
    
    while queue:
        x, y, dist = queue.popleft()

        if (x == n-1) and (y == m-1):
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n and 0 <= ny < m) and (maps[nx][ny]!=0):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
    return -1