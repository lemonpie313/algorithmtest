function solution(t, p) {
    let count = t.split("").reduce((acc, cur, idx) => {
        let comp = t.substr(idx,p.length);
        if ((comp.length==p.length)&&(Number(p) >= Number(comp))) {
            return acc+1;
        }
        return acc;
    }, 0)
    return count;
}