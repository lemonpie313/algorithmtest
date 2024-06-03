function solution(survey, choices) {
  let answer = "";
  let obj = {
    "R": 0,
    "T": 0,
    "C": 0,
    "F": 0,
    "J": 0,
    "M": 0,
    "A": 0,
    "N": 0,
  }
  let response = [0, 3, 2, 1, 0, 1, 2, 3];
  for (i in survey) {
    let select1 = survey[i].split("")[0];
    let select2 = survey[i].split("")[1];
    if (choices[i]<4) {
      obj[`${select1}`] += response[choices[i]];
    } else {
      obj[`${select2}`] += response[choices[i]];
    }
  }
  answer+=(obj["R"]>=obj["T"] ? "R" : "T")
  answer+=(obj["C"]>=obj["F"] ? "C" : "F")
  answer+=(obj["J"]>=obj["M"] ? "J" : "M")
  answer+=(obj["A"]>=obj["N"] ? "A" : "N")

  return answer;
}