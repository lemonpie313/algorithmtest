function solution(s, n) {
    var upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var lower = "abcdefghijklmnopqrstuvwxyz";

    return s.split("").map((cur) => {
        if (cur == " ") {
            return " ";
        }
        var textArr = upper.includes(cur) ? upper : lower;
        var index = (textArr.indexOf(cur) + n) % textArr.length;
        return textArr[index];

    }).join("");
}