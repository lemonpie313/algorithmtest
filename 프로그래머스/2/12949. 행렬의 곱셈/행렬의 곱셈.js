function solution(arr1, arr2) {
  let a = arr1.length;
  let b = arr2.length;
  let c = arr2[0].length;
  let ans = [];
  let aa;
  for (let i = 0; i < a; i++) {
    aa = [];
    for (let k = 0; k < c; k++) {
      let sum = 0;
      for (let j = 0; j < b; j++) {
        sum += arr1[i][j] * arr2[j][k];
      }
      aa.push(sum);
    }
    ans.push(aa);
  }
  return ans;
}