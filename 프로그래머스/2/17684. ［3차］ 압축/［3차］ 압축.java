import java.util.*;
class Solution {
    public int[] solution(String msg) {
        
        
        Map<String, Integer> dictionary = new HashMap<>();
        String[] alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
        for (int i=0; i<alphabet.length; i++) {
            dictionary.put(alphabet[i], i+1);
        }
        int lastNum = 26;
        
        // String[] msgArr = msg.split("");
        int[] answer = new int[msg.length()];
        
        int i=0;
        int idx1 = 0;
        int idx2 = 0;
        
        while (idx1 < msg.length() && idx2 < msg.length()) {
            
            String msgForFind = msg.substring(idx1, idx2 + 1);
            // System.out.println(msgForFind);
            if (dictionary.keySet().contains(msgForFind)) {
                answer[i] = dictionary.get(msgForFind);
                idx2 += 1;
                
                // System.out.println("answer[i]: " + answer[i]);
                
            } else {
                dictionary.put(msgForFind, lastNum+1);
                // System.out.println("put in dictionary: " + (lastNum+1));
                // System.out.println("-------");
                lastNum += 1;
                
                idx1 = idx2;
                i += 1;
            }
        }
        
        int leng = answer.length;
        
        for (int k=0; k<answer.length; k++) {
            if (answer[k] == 0) {
                leng = k;
                break;
            }
        }
        
        int[] answer1 = new int[leng];
        
        for (int j=0; j<leng; j++) {
            answer1[j] = answer[j];
        }
        
        return answer1;
    }
}