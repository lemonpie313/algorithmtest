import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        
        Arrays.sort(phone_book);
        
        for (int i=1; i<phone_book.length; i++) {
            if (phone_book[i].length() <= phone_book[i-1].length()) {
                continue;
            }
            if (phone_book[i].substring(0, phone_book[i-1].length()).equals(phone_book[i-1])) {
                return false;
            }
            
        }
        boolean answer = true;
        return answer;
    }
}