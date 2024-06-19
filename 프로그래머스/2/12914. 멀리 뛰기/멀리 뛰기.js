function solution(n) {
  let n1 = 1;
  let n2 = 1;
  let n3;
  if (n==0 || n==1) return 1;
  for (let i=2; i<=n; i++) {
    n3 = n1;
    n1 = (n1+n2)%1234567;
    n2 = n3;
  }
  return n1;
}