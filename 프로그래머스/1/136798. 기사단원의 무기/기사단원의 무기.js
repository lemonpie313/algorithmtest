function solution(number, limit, power) {
  let sum=0;
  for (let num = 1; num <= number; num++) {
    let cnt = 0;
    let index = 1;
    while (index <= Math.sqrt(num)) {
      if (num % index === 0) {
        cnt += 1;
        if (num / index !== index) cnt += 1;
      }
      index++;
    }
    if (cnt<=limit) {
      sum+=cnt;
    } else {
      sum+=power;
    }
  }
  return sum ;
}