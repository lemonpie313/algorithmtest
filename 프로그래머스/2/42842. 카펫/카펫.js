function solution(brown, yellow) {
  for (let i=1; i<=Math.floor(Math.sqrt(yellow)); i++) {
    if (yellow%i!=0) continue;
    let j = yellow/i;
    if (brown == 4+(i+j)*2) {
      return [j+2, i+2];
    }
  }
}