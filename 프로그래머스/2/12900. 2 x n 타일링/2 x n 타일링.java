class Solution {
    public int solution(int num) {
        int[] arr = new int[num+1];
        arr[1] = 1;
        arr[2] = 2;
        
        for (int i=3; i<=num; i++) {
            arr[i] = (arr[i-1] + arr[i-2]) % 1000000007;
        }
        
        return arr[num];
    }
}