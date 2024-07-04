function solution(k, dungeons) {
  let answer = [];
  let visited = Array(dungeons.length).fill(false);

  function dfs(cnt, k) {
    answer.push(cnt);
    for (let i = 0; i < dungeons.length; i++) {
      let cur = dungeons[i];
      if (k >= cur[0] && !visited[i]) {
        visited[i] = true;
        dfs(cnt + 1, k - cur[1]);
        visited[i] = false;
      }
    }
  }
  dfs(0, k);
  return Math.max(...answer);
}