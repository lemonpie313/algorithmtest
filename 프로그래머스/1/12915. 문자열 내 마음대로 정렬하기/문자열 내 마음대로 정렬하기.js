function solution(s, n) {

    let ss = s.map((a) => {
        return a[n]+a;
    }).sort().map((a) => {
        return a.slice(1);
    })
    return ss;
}