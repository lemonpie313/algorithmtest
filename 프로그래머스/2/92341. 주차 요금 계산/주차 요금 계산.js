function solution(fees, records) {
  const inTime = new Object();
  const times = new Object();
  records.forEach((cur) => {
    cur = cur.split(" ");
    cur[0] = cur[0].split(":").map((i) => Number(i));
    if (cur[2] == "IN") {
      inTime[cur[1]] = [cur[0], cur[2]];
    } else {
      const time =
        cur[0][0] * 60 +
        cur[0][1] -
        (inTime[cur[1]][0][0] * 60 + inTime[cur[1]][0][1]);
      times[cur[1]] = times[cur[1]] ? times[cur[1]] + time : time;
      inTime[cur[1]] = false;
    }
  });
  let arr = [];
  for (key of Object.keys(inTime)) {
    if (inTime[key]) {
      const time = 24 * 60 - 1 - (inTime[key][0][0] * 60 + inTime[key][0][1]);
      times[key] = times[key] ? times[key] + time : time;
    }
    if (times[key] > fees[0]) {
      arr.push([
        key,
        fees[1] + Math.ceil((times[key] - fees[0]) / fees[2]) * fees[3],
      ]);
    } else {
      arr.push([key, fees[1]]);
    }
  }
  return arr.sort().map((cur) => cur[1]);
}