function solution(t) {
    let a=0;
    let b=0;
    t=t.map((cur) => {
        return cur.sort((a,b)=>{return b-a});
    }).forEach((i) => {
        if (i[0]>a) {
            a=i[0];
        }
        if (i[1]>b) {
            b=i[1];
        }
    })
    return a*b;
}