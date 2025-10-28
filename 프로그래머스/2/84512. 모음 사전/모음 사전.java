class Solution {

    public int solution(String word) {
        String vowel = "AEIOU";
        int[] weight = new int[vowel.length() + 1];

        for (int i = vowel.length() - 1; i >= 0; i--) {
            weight[i] = weight[i + 1] * 5 + 1; // 자리별 가중치 계산
        }

        int answer = 0;

        for (int i = 0; i < word.length(); i++) {
            // 각 자리에서 해당 문자 인덱스 × 가중치 누적
            answer += weight[i] * vowel.indexOf(word.charAt(i));
        }

        return answer + word.length(); // 자기 자신까지 포함한 순번 보정
    }
}