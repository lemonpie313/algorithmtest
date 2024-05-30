function solution(s, skip, index) {
  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let replacedAlphabet = skip.split("").reduce((acc, cur)=> {
    return acc.replace(cur, "");
  }, alphabet).repeat(5).split("");

  let ans = s.split("").map((cur) => {
    return replacedAlphabet[replacedAlphabet.indexOf(cur)+index];
  }).join("");
  return ans;
}