function solution(clothes) {
  let obj = {};
  clothes.forEach((i) => {
    if (obj[i[1]]) obj[i[1]].push(i[0]);
    else obj[i[1]] = [i[0]];
  })
  let ans = 1;
  Object.keys(obj).forEach((i) => {
    ans *= (obj[i].length+1);
  })
  return ans-1;
}