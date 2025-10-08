from collections import deque

def solution(n, computers):
    nets = {}
    for i in range(n):
        nets[i] = []
        for j in range(0, n):
            if computers[i][j] == 1:
                nets[i].append(j)
                
    visited = set([])
    cnt = 0

    for i in range(n):
        if i not in visited:
            queue = deque([i])
            cnt += 1
            visited.add(i)
            while queue:
                node = queue.popleft()
                if nets[node] != []:
                    for next_node in nets[node]:
                        if next_node not in visited:
                            visited.add(next_node)
                            queue.append(next_node)
    
    return cnt