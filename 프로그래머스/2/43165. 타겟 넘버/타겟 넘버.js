function solution(numbers, target) {
  const plus = function (sum, numbers, i) {
    sum += numbers[i];
    if (i == numbers.length - 1 && sum == target) {
      cnt += 1;
    } else if (i != numbers.length - 1) {
      plus(sum, numbers, i + 1);
      minus(sum, numbers, i + 1);
    }
  };
  const minus = function (sum, numbers, i) {
    sum -= numbers[i];
    if (i == numbers.length - 1 && sum == target) {
      cnt += 1;
    } else if (i != numbers.length - 1) {
      plus(sum, numbers, i + 1);
      minus(sum, numbers, i + 1);
    }
  };
  let cnt = 0;
  plus(0, numbers, 0);
  minus(0, numbers, 0);

  return cnt;
}