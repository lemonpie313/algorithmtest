function solution(x) {
  return x.map((cur) => {
    const eachX = ("0" + String(cur.toString(2))).split("").reverse();
    for (let idx in eachX) {
        const nextIdx = Number(idx)+1;
      if (eachX[idx] == "0") {
        eachX[idx] = "1";
        return parseInt(eachX.reverse().join(""), 2);//.parseInt(2);
      } 
      if (eachX[idx] == "1" && eachX[nextIdx] == "0") {
        eachX[idx] = "0";
        eachX[nextIdx] = "1";
        return parseInt(eachX.reverse().join(""), 2);//.parseInt(2);
      }
      
    }
  });
}