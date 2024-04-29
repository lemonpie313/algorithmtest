function solution(a) {
    let sum = 0;
    let b = String(a).split("");
    b.forEach((i)=>{ sum+=Number(i) });
    return !(Boolean(a%sum));
}