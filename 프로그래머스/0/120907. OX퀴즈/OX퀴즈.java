import java.util.Arrays;

class Solution {
    public String[] solution(String[] quiz) {
        int answer = 0;
        int result = 0;
        String nomial;
        String[] numbers = new String[2];
        String[] questionArr = new String[2];
        String[] results = new String[quiz.length];
        int idx = 0;
        for (String question : quiz) {
            questionArr = question.split(" \\= ");
            nomial = questionArr[0];
            answer = Integer.parseInt(questionArr[1]);
            if (nomial.contains(" - ")) {
                numbers = nomial.split(" \\- ");
                result = Integer.parseInt(numbers[0]) - Integer.parseInt(numbers[1]);
            } else if (nomial.contains(" + ")) {
                numbers = nomial.split(" \\+ ");
                result = Integer.parseInt(numbers[0]) + Integer.parseInt(numbers[1]);
            }
            // results[idx] = Integer.toString(result);
            if (result == answer) {
                results[idx] = "O";
            } else {
                results[idx] = "X";
            }
            idx += 1;
        }
        
        return results;
    }
}