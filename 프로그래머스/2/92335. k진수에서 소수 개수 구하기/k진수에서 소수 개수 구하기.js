function solution(n, k) {
  const num = String(n.toString(k))
    .split("0")
    .map((cur) => Number(cur))
    .filter((cur) => {
      if (cur <= 1 || cur == NaN) return false;
      for (let i = 2; i <= Math.sqrt(cur); i++) {
        if (cur % i == 0) {
          return false;
        }
      }
      return true;
    });
  return num.length;
}
