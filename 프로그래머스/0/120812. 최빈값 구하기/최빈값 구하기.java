import java.util.Map;
import java.util.HashMap;

class Solution {
    public int solution(int[] array) {
        Map<Integer, Integer> hashMap = new HashMap<>();
        for (int a: array) {
            if (hashMap.containsKey(a)) {
                hashMap.put(a, hashMap.get(a)+1);
            } else {
                hashMap.put(a, 1);
            }
        }
        int answer = -1;
        int maxCount = 0;
        for (int key: hashMap.keySet()) {
            int counts = hashMap.get(key);
            if (maxCount < counts) {
                maxCount = counts;
                answer = key;
            } else if (maxCount == counts) {
                answer = -1;
            }
        }
        return answer;
    }
}