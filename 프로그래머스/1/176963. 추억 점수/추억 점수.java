import java.util.*;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        
        Map<String, Integer> maps = new HashMap<>();
        
        for (int i=0; i<name.length; i++) {
            maps.put(name[i], yearning[i]);
        }
        
        int[] answer = new int[photo.length];
        int sum = 0;
        for (int i=0; i<photo.length; i++) {
            sum = 0;
            for (int j=0; j<photo[i].length; j++) {
                if (maps.keySet().contains(photo[i][j])) {
                    sum += maps.get(photo[i][j]);
                }
                
            }
            answer[i] = sum;
        }
        return answer;
    }
}