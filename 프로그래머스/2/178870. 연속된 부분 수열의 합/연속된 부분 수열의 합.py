def solution(sequence, k):
    n = len(sequence)
    left = 0
    cursum = 0
    best = [0, len(sequence)-1]
    
    for right in range(n):
        cursum += sequence[right]
        
        while cursum > k and left < right:
            cursum -= sequence[left]
            left += 1
        if cursum == k:
            # print("left right: " + str(left) + " " + str(right))
            if best[1]-best[0] > right - left or (best[1]-best[0] == right - left and best[0] > left):
                best = [left, right]
    return best
