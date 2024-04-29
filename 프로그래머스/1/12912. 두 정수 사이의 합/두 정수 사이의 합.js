function solution(a, b) {
    let sum=0;
    let aa = (a>b)?a:b;
    let bb = (a>b)?b:a;
    for (let i=bb; i<=aa; i++) {
        sum+=i;
    }
    return sum;
}