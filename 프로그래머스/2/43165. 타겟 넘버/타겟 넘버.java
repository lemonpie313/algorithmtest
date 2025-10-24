class Solution {
    public static int dfs(int[] numbers, int i, int target, int result) {
        if (i == numbers.length) {
            if (result == target) {
                return 1;
            } else {
                return 0;
            }
        }
        int plusresult = result + numbers[i];
        int minusresult = result - numbers[i];
        return dfs(numbers, i+1, target, plusresult) + dfs(numbers, i+1, target, minusresult);
        
        
    }
    public int solution(int[] numbers, int target) {
        
        
        int answer = 0;
        return dfs(numbers, 0, target, 0);
    }
}