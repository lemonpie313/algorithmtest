import java.util.*;
class Solution {
    public int solution(int[] nums) {
        
        Map<Integer, Integer> numbers = new HashMap<>();
        
        for (int i: nums) {
            if (numbers.keySet().contains(i)) {
                numbers.put(i, numbers.get(i) + 1);
            } else {
                numbers.put(i, 1);
            }
        }
        
        if (nums.length / 2 > numbers.keySet().size()) {
            return numbers.keySet().size();
        }
        
        return nums.length / 2;
    }
}