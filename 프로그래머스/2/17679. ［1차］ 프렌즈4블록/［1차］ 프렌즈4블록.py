def solution(m, n, board):
    board.reverse()
    answer=  0
    
    while True:
    
        removers = []

        for i in range(m):
            board[i] = list(board[i])

        for i in range(m-1, 0, -1):
            for j in range(1, n):
                if (board[i-1][j]==board[i][j]==board[i-1][j-1]==board[i][j-1]) and board[i][j] != '0':
                    removers.append([i, j])

        if len(removers) == 0:
            break

        removedset = set()

        for remover in removers:
            locx, locy = remover[0], remover[1]

            for i in range(locx, locx-2, -1):
                for j in range(locy-1, locy+1):
                    if str(i) + " " + str(j) in list(removedset):
                        continue
                    
                    answer += 1
                    if i+1 < m:
                        for k in range(i, m-1):
                            board[k][j] = board[k+1][j]
                        board[m-1][j] = '0'
                    else:
                        board[i][j] = '0'

                    removedset.add(str(i)+" "+str(j))
        
        
    return answer