let s = "[](){}";

function solution(s) {
  let [a1, a2, b1, b2, c1, c2] = ["[", "]", "{", "}", "(", ")"];
  let cnt = 0;
  for (let i = 0; i < s.length; i++) {
    let arr = [];
    let newS = s.slice(i) + s.slice(0, i);
    let isClosed = true;
    for (let k = 0; k < newS.length; k++) {
      if (newS[k] == a1) arr.push(a1);
      else if (newS[k] == b1) arr.push(b1);
      else if (newS[k] == c1) arr.push(c1);
      else if (newS[k] == a2 && arr[arr.length - 1] == a1) {
        arr.pop();
      } else if (newS[k] == b2 && arr[arr.length - 1] == b1) {
        arr.pop();
      } else if (newS[k] == c2 && arr[arr.length - 1] == c1) {
        arr.pop();
      } else {
        isClosed = false;
        break;
      }
    }
    if (isClosed && arr.length==0) {
      cnt += 1;
      console.log(cnt);
    }
  }
  return cnt;
}

console.log(solution(s));
