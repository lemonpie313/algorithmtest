import java.util.Arrays;

class Solution {
    public String[] solution(String[] quiz) {
        String[] result = new String [quiz.length];
        for (int i = 0; i < quiz.length; i++ ) {
            String[] quizArray = quiz[i].split(" ");
            int answer = Integer.parseInt(quizArray[0]) + (Integer.parseInt(quizArray[2]) * (quizArray[1].equals("+") ? 1 : -1));
            result[i] = (answer == Integer.parseInt(quizArray[4])) ? "O" : "X";
        }
        
        return result;
    }
}