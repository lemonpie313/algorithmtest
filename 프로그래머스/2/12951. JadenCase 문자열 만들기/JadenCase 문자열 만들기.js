function solution(s) {
  return s
    .split(" ")
    .map((cur) => {
      if (cur == "") {
        return cur;
      }
      cur = cur.toLowerCase().split("");
      cur[0] = cur[0].toUpperCase();
      return cur.join("");
    })
    .join(" ");
}