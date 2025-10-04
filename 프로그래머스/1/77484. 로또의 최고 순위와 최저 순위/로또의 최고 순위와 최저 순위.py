def solution(lottos, win_nums):
    zeros = 0
    correct = 0
    for i in lottos:
        if i == 0:
            zeros += 1
        if i in win_nums:
            correct += 1
    maxcorrect = correct + zeros
    mincorrect = correct
    minrank = min([6, 7-mincorrect])
    maxrank = min([6, 7-maxcorrect])
    
    answer = [maxrank, minrank]
    return answer