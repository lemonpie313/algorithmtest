import java.util.*;
class Solution {
    public String solution(String number, int k) {
        Stack<String> st = new Stack();
        String[] nums = number.split("");
        int i = 0;
        while (k > 0 && i < nums.length) {
            // System.out.println("i: " + i);
            // System.out.println("숫자: " + nums[i]);
            if (st.empty()) {
                st.add(nums[i]);
                // System.out.println("빈배열이었슨");
                // System.out.println(String.join("", st));
                i += 1;
                continue;
            }
            if (Integer.parseInt(st.peek()) < Integer.parseInt(nums[i])) {
                st.pop();
                // System.out.println("뺐슨");
                // System.out.println(String.join("", st));
                k -= 1;
                // if (k==0 && i == nums.length-1) st.add(nums[i]);
            } else {
                st.add(nums[i]);
                // System.out.println("넣었슨");
                // System.out.println(String.join("", st));
                i += 1;
            }
        }
        
        if (i <= nums.length -1) {
            for (int j=i; j<nums.length; j++) {
                st.add(nums[j]);
            }
        } else if (k > 0) {
            for (int l=0; l<k; l++) {
                st.pop();
            }
        }
        
        String answer = String.join("", st);
        
        return answer;
    }
}