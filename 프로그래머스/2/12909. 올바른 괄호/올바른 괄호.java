import java.util.*;

class Solution {
    boolean solution(String s) {
        
        Stack opened = new Stack();
        
        for (int i=0; i<s.length(); i++) {
            if (s.substring(i, i+1).equals("(")) {
                opened.push(1);
            } else {
                if (opened.empty()) {
                    return false;
                }
                opened.pop();
            }
        }
        
        // System.out.println(Arrays.toString(opened.toArray()));
        
        if (opened.toArray().length == 0) {
            return true;
        }

        return false;
    }
}