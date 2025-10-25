import heapq
def solution(n, k, enemy):
    maxE = []
    for i in range(len(enemy)):
        heapq.heappush(maxE, (-1) * enemy[i])
        # print(str(i) + "번째 라운드")
        # print("n: " + str(n))
        # print("enemy: " + str(enemy[i]))
        # print("maxE: " + str(maxE))
        
        if n >= enemy[i]:
            n-=enemy[i]
            # print("잔여 n: " + str(n))
            # print("-----")
        else:
            if k>0:
                k-=1
                n-=enemy[i]
                n-=heapq.heappop(maxE)
                # print("잔여 maxE: " + str(maxE))
                # print("잔여 n: " + str(n))
                # print("-----")
            else:
                return i

    return len(enemy)