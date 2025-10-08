from heapq import heappush, heappop
def solution(n, works):
    heap = []
    for work in works:
        heappush(heap, -work)

    for i in range(n):
        if len(heap)==0:
            return 0
        work = heappop(heap)
        work+=1
        if work != 0:
            heappush(heap, work)

    sums = 0
    for i in heap:
        sums += i**2
            
    return sums