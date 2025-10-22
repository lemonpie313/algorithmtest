import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> result = new Stack();
        
        for (int i=0; i<arr.length; i++) {
            if (i==0) {
                result.push(arr[i]);
            } else {
                if (result.peek().equals(arr[i])) {
                    continue;
                }
                result.push(arr[i]);
            }
        }
        int[] answer = new int[result.size()];
        for (int i=0; i<result.size(); i++) {
            answer[i] = result.get(i);
        }

        return answer;
    }
}