function solution(lottos, win_nums) {
  let [zero, match] = lottos.reduce(([zero, match], cur) => {
    if (cur==0) {
      return [zero+1, match];
    } else if (win_nums.includes(cur)) {
      return [zero, match+1];
    }
    return [zero, match];
  }, [0, 0]);

  let rank = [6, 6, 5, 4, 3, 2, 1];
  return [rank[zero+match], rank[match]];
  
}