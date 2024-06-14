function solution(s) {
  let zero = 0;
  let cnt = 0;
  while (s.length!=1) {
    const s1 = s.replaceAll("0", "");
    const c = s1.length;
    zero = zero + s.length - c;
    cnt+=1;
    s=c.toString(2);
  }
  return [cnt, zero];
}