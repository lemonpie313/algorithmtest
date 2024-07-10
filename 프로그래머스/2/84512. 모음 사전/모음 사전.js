function solution(word) {
  const num = [781, 156, 31, 6, 1];
  const letter = ['A','E','I','O','U'];
  return word.split("").reduce((acc, cur, idx, arr) => {
    return acc + letter.indexOf(cur) * num[idx];
  }, 0) + word.length;
}