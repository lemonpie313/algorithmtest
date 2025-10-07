import heapq
def solution(scoville, K):
    cnt = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    
    while heap[0]<K:
        if len(heap)==1:
            return -1
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        heapq.heappush(heap, one+two*2)
        cnt+=1
    return cnt
    
        