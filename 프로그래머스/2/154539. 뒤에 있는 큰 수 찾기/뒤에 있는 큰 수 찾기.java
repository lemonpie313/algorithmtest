import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        
        Stack<Integer> stack = new Stack<>();
        
        stack.push(numbers[numbers.length-1]);
        
        int[] result = new int[numbers.length];
        
        result[numbers.length-1] = -1;
        
        for (int i=numbers.length-2; i>=0; i--) {
            if (numbers[i] >= stack.get(0)) {
                result[i] = -1;
                stack = new Stack<>();
                stack.push(numbers[i]);
            } else {
                for (int j=stack.size()-1; j>=0; j--) {
                    int st = stack.get(j);
                    if (st > numbers[i]) {
                        result[i] = st;
                        stack.push(numbers[i]);
                        break;
                    } else {
                        stack.pop();
                    }
                }
            }            
        }
        return result;
    }
}