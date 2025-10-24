import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int width = 0;
        int height = 0;
        int[] answer = new int[2];
        
        for (int i=1; i<=Math.sqrt(yellow); i++) {
            if (yellow % i == 0) {
                width = yellow / i;
                height = i;
                if (brown == (width + height) * 2 + 4) {
                    answer[0] = width+2;
                    answer[1] = height+2;
                    break;
                }
            }
        }
        
        
        return answer;
    }
}