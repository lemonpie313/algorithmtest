import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        
        Arrays.sort(people);
        for (int i=0; i<people.length/2; i++ ) {
            int temp = people[i];
            people[i] = people[people.length-i-1];
            people[people.length-i-1] = temp;
        }
        
        int endindex = people.length -1;
        int answer = 0;
        
        // System.out.println(Arrays.toString(people));
        
        for (int i=0; i < people.length; i++ ) {
            if (people[i] + people[endindex] <= limit) {
                endindex -= 1; 
            }
            answer += 1;
            if (endindex <= i) {
                break;
            }
        }
        
        
        return answer;
    }
}