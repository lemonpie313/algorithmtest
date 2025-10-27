import java.util.*;
class Solution {
    public int solution(String[] maps) {
        Queue<int[]> qq = new ArrayDeque();
        Queue<int[]> qqq = new ArrayDeque();
        
        String[][] newMap = new String[maps.length][maps[0].length()];
        boolean[][] visited_bf_l = new boolean[maps.length][maps[0].length()];
        boolean[][] visited_af_l = new boolean[maps.length][maps[0].length()];
        
        for (int i=0; i<maps.length; i++) {
            newMap[i] = maps[i].split("");
            for (int j=0; j<newMap[i].length; j++) {
                visited_bf_l[i][j] = false;
                visited_af_l[i][j] = false;
                if (newMap[i][j].equals("S")) {
                    int[] start = {i, j, 0};
                    qq.add(start);
                }
                if (newMap[i][j].equals("L")) {
                    int[] start = {i, j, 0};
                    qqq.add(start);
                }
            }
        }
        
        int[] dx = {1,0,-1,0};
        int[] dy = {0,1,0,-1};
        
        int labber = 0;

        while (!qq.isEmpty()) {
            int[] nxt = qq.poll();
            
            // System.out.println(nxt[0] + " " + nxt[1] + " " + nxt[2]);
            
            if (nxt[0]<0 || nxt[0]>=newMap.length || nxt[1]<0 || nxt[1]>=newMap[0].length || newMap[nxt[0]][nxt[1]].equals("X") || visited_bf_l[nxt[0]][nxt[1]] == true) {
                // System.out.println("성립x");
                continue;
            } else if (newMap[nxt[0]][nxt[1]].equals("L")) {
            labber = nxt[2];
            break;
            }
            visited_bf_l[nxt[0]][nxt[1]] = true;
              
            for(int i=0; i<4; i++) {
                int[] nxt_path = new int[3];
                nxt_path[0] = nxt[0] + dx[i];
                nxt_path[1] = nxt[1] + dy[i];
                nxt_path[2] = nxt[2] + 1;
                qq.add(nxt_path);
            }
        }
        
        // System.out.println("----" + labber);
        
        int exit = 0;
        
        while (!qqq.isEmpty()) {
            int[] nxt = qqq.poll();
            
            // System.out.println(nxt[0] + " " + nxt[1] + " " + nxt[2]);
            
            if (nxt[0]<0 || nxt[0]>=newMap.length || nxt[1]<0 || nxt[1]>=newMap[0].length || newMap[nxt[0]][nxt[1]].equals("X") || visited_af_l[nxt[0]][nxt[1]] == true) {
                // System.out.println("성립x");
                continue;
            } else if (newMap[nxt[0]][nxt[1]].equals("E")) {
            exit = nxt[2];
            break;
            }
            
            visited_af_l[nxt[0]][nxt[1]] = true;
              
            for(int i=0; i<4; i++) {
                int[] nxt_path = new int[3];
                nxt_path[0] = nxt[0] + dx[i];
                nxt_path[1] = nxt[1] + dy[i];
                nxt_path[2] = nxt[2] + 1;
                qqq.add(nxt_path);
            }
        }
        
        if (labber == 0 || exit == 0) {
            return -1;
        }
        return labber + exit;
    }
}