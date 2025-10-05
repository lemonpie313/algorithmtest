def solution(board, moves):
    results = []
    depth = len(board)
    cnt=0
    for i in moves:
        for j in range(depth):
            grabbed = board[j][i-1]
            if grabbed != 0:
                board[j][i-1]=0
                break
                
        if grabbed == 0:
            continue
        if (len(results)!=0) and (results[-1] == grabbed):
            results.pop()
            cnt+=2
        else:
            results.append(grabbed)
               
    return cnt