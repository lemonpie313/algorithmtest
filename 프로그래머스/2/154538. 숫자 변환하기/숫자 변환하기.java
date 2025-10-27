import java.util.*;
class Solution {
    public int solution(int x, int y, int n) {
        int turn = 0;
        
        Integer[] xAndTurn = {x, turn};
        
        Queue<Integer[]> xx = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        visited.add(x);
        xx.add(xAndTurn);
        
        while (!(xx.isEmpty())) {
            Integer[] next_x = xx.poll();
            x = next_x[0];
            turn = next_x[1];
            if (x==y) {
                return turn;
            }
            turn += 1;
            
            if (x*2<=y && visited.add(x*2)) {
                Integer[] next_x_1 = {x*2, turn};
                xx.add(next_x_1);
            }
            if (x*3<=y && visited.add(x*3)) {
                Integer[] next_x_2 = {x*3, turn};
                xx.add(next_x_2);           
            }
            if (x+n<=y && visited.add(x+n)) {
                Integer[] next_x_3 = {x+n, turn};
                xx.add(next_x_3);
            }
        }
        
        return -1;
    }
}