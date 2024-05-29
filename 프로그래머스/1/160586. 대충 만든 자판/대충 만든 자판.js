function solution(keymap, targets) {
  let ans = targets.map((current) => {
    let acc = current.split("").reduce((acc, cur, idx, src) => {
      let cnt = 101;
      keymap.forEach((i) => {
        let icnt = i.split("").indexOf(cur);
        if (icnt != -1) {
          cnt = cnt > icnt ? icnt : cnt;
        }
      });
      if (cnt>100) {
        src.splice(idx);
        return -1;
      } else {
        return acc + cnt + 1;
      }
    }, 0);
    return acc;
  });

  return ans;
}