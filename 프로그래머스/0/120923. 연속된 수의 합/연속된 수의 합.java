import java.util.stream.IntStream;

class Solution {
    public int[] solution(int num, int total) {
        int firstnum = 0;
        int middlenum = 0;
        int endnum = 0;
        if (total % num == 0) {
            middlenum = total / num;
            firstnum = middlenum - (num / 2);
            endnum = middlenum + (num / 2);
            
        } else {
            middlenum = total / num;
            firstnum = middlenum - (num / 2) + 1;
            endnum = middlenum + (num / 2);
        }
        int[] answer = IntStream.rangeClosed(firstnum, endnum).toArray();
        return answer;
    }
}