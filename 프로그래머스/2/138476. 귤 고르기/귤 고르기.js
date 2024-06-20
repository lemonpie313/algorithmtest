function solution(k, tangerine) {
  let numOfTangerine = {};
  let cnt = 0;
  for (let t of tangerine) {
    numOfTangerine[t] = numOfTangerine[t] ? numOfTangerine[t] + 1 : 1;
  }
  let nums = Object.values(numOfTangerine).sort((a, b) => b - a);
  for (let num of nums) {
    k-=num;
    cnt+=1;
    if (k<=0) break;
  }
  return cnt;
}