import java.util.*;
class Solution {

    String[] numberArr;
    Set<Integer> prime;

    public int solution(String numbers) {
        this.numberArr = numbers.split("");
        this.prime = new HashSet<>();

        // 각 숫자를 시작점으로 DFS 수행 (모든 자리수 조합 생성)
        for (int i = 0; i < numbers.length(); i++) {
            String num = numberArr[i];
            Set<String> visited = new HashSet<>();

            visited.add(num);
            dfs(num, 1 << i, visited);
        }

        return prime.size();
    }

    // DFS로 숫자 조합을 만들며 소수 판별 및 저장
    public void dfs(String num, int mask, Set<String> visited) {
        int n = Integer.parseInt(num);
        if (!prime.contains(n) && isPrime(n)) prime.add(n);

        for (int i = 0; i < numberArr.length; i++) {
            if (((1 << i) & mask) != 0) continue; // 이미 사용된 숫자면 건너뜀

            String nextNum = num + numberArr[i];
            if (visited.contains(nextNum)) continue; // 동일 숫자 조합 중복 방지

            visited.add(nextNum);
            dfs(nextNum, mask | (1 << i), visited);
            visited.remove(nextNum); // 백트래킹
        }
    }

    // 소수 판별
    public boolean isPrime(int num) {
        if (num == 2) return true;
        if (num == 1 || num % 2 == 0) return false;

        for (int i = 3; i <= Math.sqrt(num); i += 2) {
            if (num % i == 0) return false;
        }

        return true;
    }

}