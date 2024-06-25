function solution(citations) {
  let ans = 0;
  for (let i = 1; i<=citations.length; i++) {
    let up = citations.filter((cur) => cur >= i);
    if (up.length >= i) {
      ans = i;
    }
  }
  return ans;
}