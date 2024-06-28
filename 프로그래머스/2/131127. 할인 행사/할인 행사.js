function solution(want, number, discount) {
  let cnt=0;
  for (let i=0; i<=discount.length-10; i++) {
    const disdays = discount.slice(i, i+10);
    const signup = want.every((item, idx) => {
      return disdays.filter((disitem) => disitem==item).length >= number[idx]
    }
    )
    if (signup) cnt+=1;
  }
  return cnt;
}