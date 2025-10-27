import java.util.*;
class Solution {    
    public long solution(int[] weights) {
        
        Map<Integer, Integer> sets = new HashMap<>();
        Map<Integer, Integer> sames = new HashMap<>();
        
        long answer = 0;
        
        for (int i=0; i<weights.length; i++) {
            int a = weights[i];
            // System.out.println("======" + a);
            
            int b = a*2;
            int c = a*3;
            int d = a*4;
            if (sets.keySet().contains(b)) {
                // System.out.println("*2");
                // System.out.println(sets.get(b));
                answer += sets.get(b);
                sets.put(b, sets.get(b)+1);
            } else {
                sets.put(b, 1);
            }
            if (sets.keySet().contains(c)) {
                // System.out.println("*3");
                // System.out.println(sets.get(c));
                answer += sets.get(c);
                sets.put(c, sets.get(c)+1);
            } else {
                sets.put(c, 1);
            }
            if (sets.keySet().contains(d)) {
                // System.out.println("*4");
                // System.out.println(sets.get(d));
                answer += sets.get(d);
                sets.put(d, sets.get(d)+1);
            } else {
                sets.put(d, 1);
            }
            
            if (sames.keySet().contains(a)) {
                // System.out.println("=");
                // System.out.println(sames.get(a));
                answer += sames.get(a);
                answer -= (sames.get(a) * 3);
                sames.put(a, sames.get(a)+1);
            } else {
                sames.put(a, 1);
            }
            // System.out.println("-----------: " + answer);

        }
        return answer;
    }
}