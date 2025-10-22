import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        Arrays.sort(d);
        int sum = 0;
        int result = 0;
        for (int i: d) {
            if (sum + i <= budget) {
                result += 1;
                sum += i;
            } else {
                break;
            }
        }
        return result;
    }
}