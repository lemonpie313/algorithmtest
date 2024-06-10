function solution(park, routes) {
  let loc = [];
  let len = [0, 0];
  let obs = [];
  len[0] = park.length;
  park = park.map((cur, idx) => {
    cur = cur.split("");
    len[1] = cur.length;
    if (cur.includes("S")) {
      loc = [idx, cur.indexOf("S")];
    } else if (cur.includes("X")) {
      obs.push([idx, cur.indexOf("X")]);
    }
    return cur;
  });
  return routes.reduce((acc, cur, idx, arr) => {
    cur = cur.split(" ");
    cur[1] = Number(cur[1]);
    if (cur[0] == "E" && loc[1] + cur[1] < len[1]) {
      for (let i = 1; i <= cur[1]; i++) {
        if (park[loc[0]][loc[1] + i] == "X") {
          return loc;
        }
      }
      loc[1] += cur[1];
    } else if (cur[0] == "W" && loc[1] - cur[1] >= 0) {
      for (let i = 1; i <= cur[1]; i++) {
        if (park[loc[0]][loc[1] - i] == "X") {
          return loc;
        }
      }
      loc[1] -= cur[1];
    } else if (cur[0] == "N" && loc[0] - cur[1] >= 0) {
      for (let i = 1; i <= cur[1]; i++) {
        if (park[loc[0] - i][loc[1]] == "X") {
          return loc;
        }
      }
      loc[0] -= cur[1];
    } else if (cur[0] == "S" && loc[0] + cur[1] < len[0]) {
      for (let i = 1; i <= cur[1]; i++) {
        if (park[loc[0] + i][loc[1]] == "X") {
          return loc;
        }
      }
      loc[0] += cur[1];
    }
    return loc;
  }, loc);
}