import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        int i = 0;
        for (int a: query) {
            if (i%2 == 0) {
                int[] arr2 = Arrays.copyOfRange(arr, 0, query[i]+1);
                arr = arr2;
            } else {
                int[] arr2 = Arrays.copyOfRange(arr, query[i], arr.length);
                arr = arr2;
            }
            
            i+=1;
        }
        
        return arr;
    }
}