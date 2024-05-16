function solution(answers) {
  let supo1 = [1, 2, 3, 4, 5];
  let supo2 = [2, 1, 2, 3, 2, 4, 2, 5];
  let supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  let supoans = (supo) => {
    return answers.reduce((acc, cur, idx) => {
      let supoidx = idx % supo.length;
      if (cur == supo[supoidx]) {
        return acc + 1;
      }
      return acc;
    }, 0);
  };
  
  let supoans3 = [-1, supoans(supo1), supoans(supo2), supoans(supo3)];
  let max = Math.max(...supoans3);

  let answer = supoans3.map((cur, idx) => {
    if (cur==max) {
      return idx;
    } else {
      return -1;
    }
  }).filter((i) => i!=-1 );

  return answer;
}