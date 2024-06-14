function solution(n) {
  let n1 = 1;
  let n2 = 1;
  let n3;
  if (n==1 || n==2) return 1;
  for (let i=3; i<=n; i++) {
    n3 = n1;
    n1 = (n1+n2)%1234567;
    n2 = n3;
  }
  return n1%1234567;
}