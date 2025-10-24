import java.util.*;
class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        
        String[] today1 = today.split("\\.");
        int todayYear = Integer.parseInt(today1[0]);
        int todayMonth = Integer.parseInt(today1[1]);
        int todayDate = Integer.parseInt(today1[2]);
        
        Map<String, Integer> termsMap = new HashMap<>();
        
        for (int i = 0; i < terms.length; i++) {
            String[] personalTerm = terms[i].split(" ");
            termsMap.put(personalTerm[0], Integer.parseInt(personalTerm[1]));
        }
        
        List<Integer> result = new ArrayList();
        
        for (int i=0; i<privacies.length; i++) {
            String[] dateAndChar = privacies[i].split(" ");
            String person = dateAndChar[1];
            String[] date = dateAndChar[0].split("\\.");
            
            int fromYear = Integer.parseInt(date[0]);
            int fromMonth = Integer.parseInt(date[1]);
            int fromDate = Integer.parseInt(date[2]);
            
            int lastMonth = fromMonth + termsMap.get(person);
            int lastYear = fromYear;
            int lastDate = fromDate;
            
            if (lastMonth > 12 && lastMonth % 12 != 0) {
                lastYear = lastYear + lastMonth/12;
                lastMonth = lastMonth % 12;
            } else if (lastMonth % 12 == 0) {
                lastYear = lastYear + lastMonth/12 - 1;
                lastMonth = 12;
            }
            
            if (todayYear > lastYear || (todayYear == lastYear && todayMonth > lastMonth) || (todayYear == lastYear && todayMonth == lastMonth && todayDate >= lastDate)) {
                result.add(i+1);
            }
            
        }
        
        return result.stream().mapToInt(Integer::intValue).toArray();
        
    }
}