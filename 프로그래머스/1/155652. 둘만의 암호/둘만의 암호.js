function solution(s, skip, index) {
  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let replacedAlphabet = skip.split("").reduce((acc, cur)=> {
    return acc.replace(cur, "");
  }, alphabet).split("");
  let ans = s.split("").map((cur) => {
    const idx = (replacedAlphabet.indexOf(cur)+index)%replacedAlphabet.length;
    return replacedAlphabet[idx];
  }).join("");
  return ans;
}