import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        
        int n = maps.length;
        int m = maps[0].length;
        
        int[] loc = {0, 0};
        int[] fin = {maps.length-1, maps[0].length-1};
        
        Queue<int[]> qq = new ArrayDeque<>();
        
        boolean[][] visited = new boolean[n][m];
        
        int[] dx = {1,0,-1,0};
        int[] dy = {0,1,0,-1};
        
        qq.offer(new int[] {0, 0, 1});
        visited[0][0] = true;
        
        while (!qq.isEmpty()) {
            int[] a = qq.poll();
            int x = a[0];
            int y = a[1];
            int cnt = a[2];
            // System.out.println(x + " " + y);
            
            if (x == maps.length -1 && y == maps[0].length -1 ) {
                return cnt;
            }
            
            for (int i=0; i<4; i++) {
                int newx = x + dx[i];
                int newy = y + dy[i];
                // System.out.println(": " + newx + " " + newy);
                if (0 <= newx && newx < maps.length && 0 <= newy && newy < maps[0].length && maps[newx][newy] == 1 && visited[newx][newy] != true) {
                    qq.offer(new int[] {newx, newy, cnt +1});
                    visited[newx][newy] = true;
                }
            }
        }
        
        return -1;

    }
}