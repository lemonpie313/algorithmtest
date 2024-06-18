function solution(arr) {
  let getGCD = (num1, num2) => (num2 > 0 ? getGCD(num2, num1 % num2) : num1);
  for (let i=1; i<arr.length; i++) {
    let gcd = getGCD(arr[i-1], arr[i]);
    arr[i] = gcd * (arr[i-1]/gcd) * (arr[i]/gcd);
  }
  return arr[arr.length-1];
}