class Solution {
    public int[] solution(int[] sequence, int k) {
        
        int[] left_right =  {0, 0};
        int sums = sequence[0];
        int[] best = {0, 1000001};
        
        
        while (left_right[0] <= sequence.length-1 && left_right[1] <= sequence.length-1) {

            // System.out.println(sums);
            // System.out.println(left_right[0] + " " + left_right[1]);
            if (sums == k) {
                if (best[1]-best[0] > left_right[1]-left_right[0]) {
                    best = left_right.clone();
                }
                if (left_right[1] == sequence.length - 1) break;
                left_right[1] += 1;
                sums += sequence[left_right[1]];
            } else if (sums > k) {
                sums -= sequence[left_right[0]];
                
                if (left_right[0] == left_right[1]) {
                    // System.out.println("--끝--");
                    break;
                }
                left_right[0] += 1;
                // System.out.println("----");
            } else if (sums < k) {
                if (left_right[1] == sequence.length-1) break;
                left_right[1] += 1;
                sums += sequence[left_right[1]];
            }
        }
        return best;
    }
}