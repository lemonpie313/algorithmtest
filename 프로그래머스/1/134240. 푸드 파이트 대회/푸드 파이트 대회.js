function solution(s) {
    let result = "";
    let cal=1;
    let res = s.map((cur, idx) => {
        let arr = [];
        for (let i=1; i<=cur/2; i++) {
            arr.push(cal);
        }
        if (!(cur==1 && idx==0)) {
            cal+=1;
        }
        return arr.join("");
    })
    result = res.join("");
    result+="0";
    result+=res.reverse().join("");

    return result;
}