from collections import deque

def solution(queue1, queue2):
    
    quelen = len(queue1)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    answer = -1
    cnt1 = 0
    cnt2 = 0
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    resets = [-quelen]
    
    while sum1 != sum2:
        if cnt1 == cnt2 and cnt1 != 0 and cnt1 >= resets[-1] + quelen:

            resets.append(cnt1)

            if len(resets) >= 3:
                return -1
            
        if sum1>sum2:
            if len(queue1) == 1:
                return -1
            sum2 += queue1[0]
            sum1 -= queue1[0]
            queue2.append(queue1.popleft())
            cnt1 += 1
        else:
            if len(queue2) == 1:
                return -1
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
            cnt2 += 1

    return cnt1 + cnt2