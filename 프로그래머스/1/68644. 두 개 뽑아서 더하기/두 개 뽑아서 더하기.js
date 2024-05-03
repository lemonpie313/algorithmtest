function solution(s) {
    let a = [];
    for (let i = 0; i < s.length; i++) {
        for (let j = i+1; j < s.length; j++) {
            if (a.includes(s[i]+s[j])) {
                continue;
            }
            a.push(s[i] + s[j]);
            console.log(s[i] + s[j]);
        }
    }
    return a.sort((a,b)=>a-b);

}