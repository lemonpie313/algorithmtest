import java.util.*;
import java.util.regex.Pattern;

class Solution {
    public int solution(String str1, String str2) {
        
        ArrayList<String> string1 = new ArrayList();
        ArrayList<String> string2 = new ArrayList();
        
        str1 = str1.toUpperCase();
        str2 = str2.toUpperCase();
        
        for (int i=0; i<str1.length()-1; i++ ) {
            if (str1.substring(i, i+2).matches("[a-zA-Z]{2}")) {
                string1.add(str1.substring(i, i+2));
            }
        }
        
        for (int i=0; i<str2.length()-1; i++ ) {
            if (str2.substring(i, i+2).matches("[a-zA-Z]{2}")) {
                string2.add(str2.substring(i, i+2));
            }
        }
        
        if (string1.toArray().length == 0 && string2.toArray().length == 0) {
            return 1 * 65536;
        } else if (string1.toArray().length == 0 || string2.toArray().length == 0) {
            return 0;
        }
        
        int cnt = 0;
        
        ArrayList<String> temp = new ArrayList<>(string2);
        
        for (String i: string1) {
            if (temp.contains(i)) {
                cnt += 1;
                temp.remove(i);
            }
        }
        
        int cntAll = string1.size() + string2.size() - cnt;
        
        int answer = 65536 * cnt / cntAll;
        return answer;
    }
}