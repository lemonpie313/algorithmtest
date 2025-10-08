from collections import deque
def solution(n, wires):
    trees = {}
    for i in range(len(wires)):
        if wires[i][0] not in trees.keys():
            trees[wires[i][0]] = [wires[i][1]]
        else:
            trees[wires[i][0]].append(wires[i][1])
        if wires[i][1] not in trees.keys():
            trees[wires[i][1]] = [wires[i][0]]
        else:
            trees[wires[i][1]].append(wires[i][0])

    compares = []
    for i in wires:
        trees[i[0]].remove(i[1])
        trees[i[1]].remove(i[0])

        compare = []
        for j in range(2):
            queue = deque([i[j]])
            visited = set([i[j]])

            while queue:
                cur = queue.popleft()
                visited.add(cur)
                
                for nexts in trees[cur]:
                    if nexts not in visited:
                        queue.append(nexts)
    
            compare.append(len(list(visited)))
        compares.append(abs(compare[0]-compare[1]))
        trees[i[0]].append(i[1])
        trees[i[1]].append(i[0])
    return min(compares)