import java.util.*;

class Solution {
    public String[] solution(String[] records) {
        
        Map<String, String> dicts = new HashMap<>();
        
        for (String str: records) {
            
            String[] record = str.split(" ");
            
            if (record[0].equals("Leave")) continue;
            
            if (!dicts.keySet().contains(record[1])) {
                dicts.put(record[1], record[2]);
            } else if (dicts.get(record[1]) != record[2]) {
                dicts.put(record[1], record[2]);
            }
            
        }
        
        String[] result = new String[records.length];
        int i=0;
        // ArrayList<String> result = new ArrayList<>();
        
        for (String str: records) {
            
            String[] record = str.split(" ");
            // System.out.println(record[0] + record[1]);
            
            String msg = "";
            
            if (record[0].equals("Enter")) msg = "들어왔습니다.";
            else if (record[0].equals("Leave")) msg = "나갔습니다.";
            else continue;
            
            String message = dicts.get(record[1]) + "님이 " + msg;
            // System.out.println(message);
            result[i] = message;
            i += 1;
        }
        
        String[] answer = Arrays.copyOfRange(result, 0, i);
        
        return answer;
        
    }

}