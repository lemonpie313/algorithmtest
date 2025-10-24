import java.util.*;
class Solution {
    public int solution(int[] topping) {
        Map<Integer, Integer> cakeA = new HashMap<>();
        Map<Integer, Integer> cakeB = new HashMap<>();
                
        int answer = 0;
        
        for(int i=0; i<topping.length; i++) {
            if (cakeA.containsKey(topping[i])) {
                cakeA.put(topping[i], cakeA.get(topping[i]) + 1);
            } else
                cakeA.put(topping[i], 1);
        }
        
        for (int i=0; i<topping.length; i++) {
            if (cakeB.containsKey(topping[i])) {
                cakeB.put(topping[i], cakeB.get(topping[i]) + 1);
            } else
                cakeB.put(topping[i], 1);
            cakeA.put(topping[i], cakeA.get(topping[i])-1);
            if (cakeA.get(topping[i]) == 0) {
                cakeA.remove(topping[i]);
            }
            if (cakeA.keySet().size() == cakeB.keySet().size()) {
                answer += 1;
            }
                
        }

        return answer;
    }
}