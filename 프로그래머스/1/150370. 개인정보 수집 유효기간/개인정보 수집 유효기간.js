function solution(today, terms, privacies) {
  today = today.split(".").map((cur) => Number(cur));
  terms = terms.map((cur) => {
    cur = cur.split(" ");
    return [cur[0], Number(cur[1])];
  });
  return privacies.map((cur, idx) => {
    cur = cur.split(" ");
    cur[0] = cur[0].split(".");

    let [year, month, date] = [
      Number(cur[0][0]),
      Number(cur[0][1]),
      Number(cur[0][2]),
    ];
    let promise = cur[1];

    let term = terms.find((i) => i[0] == promise);
    month = month + term[1];
    
    if (date == 1) {
      month -= 1;
      date = 28;
    } else {
      date = date - 1;
    }
    console.log(month);
    if (month > 12) {
      year = (month%12==0) ? (year + Math.floor(month / 12)-1) : (year + Math.floor(month / 12));
      month = (month%12==0) ? 12 : month % 12;
    }
    console.log(year, month, date);
    if (
      year > today[0] ||
      (year == today[0] && month > today[1]) ||
      (year == today[0] && month == today[1] && date >= today[2])
    ) {
      return -1;
    }
    return idx+1;
  }).filter((i) => i!=-1);

}