function solution(s) {
    let ss = s.split("");
    let a=0;
    let b=0;
    let cur = ss[0];
    let cnt=1;
    for(let i=0; i<ss.length; i++) {
        if (a!=0 && a==b) {
            cur = ss[i];
            a=1;
            b=0;
            cnt+=1;
        }
        else if (cur==ss[i]) {
            a+=1;
        } else {
            b+=1;
        }           
    }
    return cnt;
}