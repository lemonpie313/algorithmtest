class Solution {
    public int solution(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0 ; j < board[i].length; j++) {
                if (board[i][j] == 1) {
                    if (i+1 < board.length) {
                        board[i+1][j] = board[i+1][j] == 1 ? 1 : -1;
                        if (j+1 < board[i].length) {
                            board[i+1][j+1] = board[i+1][j+1] == 1 ? 1 : -1;
                        }
                        if (j-1 >= 0) {
                            board[i+1][j-1] = board[i+1][j-1] == 1 ? 1 : -1;
                        }
                    }
                    if (i-1 >= 0) {
                        board[i-1][j] = board[i-1][j] == 1 ? 1 : -1;
                        if (j+1 < board[i].length) {
                            board[i-1][j+1] = board[i-1][j+1] == 1 ? 1 : -1;
                        }
                        if (j-1 >= 0) {
                            board[i-1][j-1] = board[i-1][j-1] == 1 ? 1 : -1;
                        }
                    }
                    if (j+1 < board[i].length) {
                        board[i][j+1] = board[i][j+1] == 1 ? 1 : -1;
                    }
                    if (j-1 >= 0) {
                        board[i][j-1] = board[i][j-1] == 1 ? 1 : -1;
                    }
                }
            }
        }
        int cnt = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0 ; j < board[i].length; j++) {
                if (board[i][j] == 0) {
                    cnt += 1;
                }
            }
        }
        return cnt;
    }
}